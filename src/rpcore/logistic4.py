'''
Created on 01.11.2013

@author: gena
'''
from __future__ import division,print_function
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from string import ascii_uppercase     
    
class Logistic4(object):
    '''
    4-parametric logistic function approximation
    '''
    name = '4PL'
    referenceCount = 4
    
    def __init__(self, x, y):
        self.fitPvals(x, y)
       
    def eval(self, x):
        '''
        return function value with stored coefficients
        '''
        return self.evalFunc(x, self.p)
    
    def invEval(self, y):
        '''
        return value for inverse function with stored coefficients
        '''
        return self.invEvalFunc(y, self.p)
    
    def evalFunc(self, x, p):
        A,B,C,D = p
        return ((A-D)/(1.0+((x/C)**B))) + D
    
    def invEvalFunc(self, y,p):
        A,B,C,D = p
        if y<=A:
            return 0
        if y>=D:
            return np.Inf
        return C*( ( (D-A)/(D-y) -1.0 )**(1/B) )
    
    def isFitted(self):
        return self.p is not None
    
    def fitPvals(self, x,y):
        '''
        Fit coefficients according to data x and y
        '''
        def residualsAbs(p, x, y):
            """Deviations of data from fitted curve"""
            err = y-self.evalFunc(x, p)
            return err
        # Create p0
        print('Fitting coefficients...')
        self.p = self.makeGuess(x, y)
        print('Guessed coefficients: ',self.p)
        # Fit equation using least squares optimization
        self.p,cov,infodict,mesg,ier = leastsq(residualsAbs,self.p,args=(x,y),
                                          full_output=True)
        print('Fitted coefficients: ',self.p)
        ss_err=(infodict['fvec']**2).sum()
        ss_tot=((y-y.mean())**2).sum()
        self.rsquared=1-(ss_err/ss_tot)
        
    def fitPlot(self, x,y):
        maxx=max(x)
        minx=min(x)
        xsize=maxx-minx
        xstart=minx-0.1*xsize
        xstop=maxx+0.1*xsize
        xx=np.linspace(minx, maxx, 50)
        plt.plot(xx,self.eval(xx),'-',x,y,'o')
        #plt.xscale('log')
        plt.xlim((xstart, xstop))
        plt.title('Least-squares {} fit, R^2={:.3f}'.format(self.name,self.rsquared))
        plt.legend([self.name+' fit', 'Reference'], loc='upper left')
        params = ascii_uppercase[:len(self.p)]
        ycor = max(y)
        ystep = (ycor-min(y))/8
        for i, (param, est) in enumerate(zip(params, self.p)):
            plt.text(minx, ycor*0.8-i*ystep, 'est({}) = {:.3f}'.format(param, est))
        
        return plt  
    
    def makeGuess(self,x,y):
        return y.min(),1.0,x.mean(),y.max()
    

#=========================================================================
def main():
    def testApproximation(approximation, x,p,noise,name='function',comment=''):
        y_true = approximation.evalFunc(x, p)
        y_meas = y_true + noise
        approximation.fitPvals(x, y_meas)
        fitPlot = approximation.fitPlot(x, y_meas)
        fitPlot.show()
    
    x = np.linspace(1,20,20)
    noise = npr.randn(len(x))
    logistic4 = Logistic4()
    p4=(7.3,2.5,10,0.5)
    for noiseLevel in (0.02,0.1,0.3) :
        testApproximation(logistic4, x, p4,noise*noiseLevel,'4PL','noiseLevel={}'.format(noiseLevel))
    
if __name__ == '__main__':
    main()
