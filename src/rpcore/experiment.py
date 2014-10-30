'''
Created on Oct 30, 2014

@author: gzakharov
'''
import numpy as np
import matplotlib.pyplot as plt
from PyQt4 import QtCore

from rpcore.sample import Sample
from rpcore.logistic4 import Logistic4

class Experiment(QtCore.QObject):
    '''
    This class holds data for set of sample with common Concentration Value
    '''
    signalConcentrationsChanged = QtCore.pyqtSignal(object)
    signalSampleAdded = QtCore.pyqtSignal(Sample)
    signalSampleRemoved = QtCore.pyqtSignal(Sample)

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(Experiment, self).__init__(parent)
        self.concentrations = None
        self.samples = {} # sample name as a key, and list of data in item
        self.referenceName = ''
        
    def setConcentrations(self, concentrations):
        self.concentrations= np.array(concentrations)
        self.signalConcentrationsChanged.emit(self.concentrations)
        
    def setReference(self, name):
        if name in self.samples.keys() :
            self.referenceName = name
        else :
            self.referenceName = ''
            
    def addSample(self, sample):
        for dataset in sample.activities :
            if len(dataset) != len(self.concentrations):
                raise
        self.samples[sample.name]=sample
        sample.setApproximation(Logistic4(self.concentrations,sample.meanActivities()))
        self.signalSampleAdded.emit(sample)
              
    def plot(self):
        maxc=max(self.concentrations)
        minc=min(self.concentrations)
        xsize=maxc-minc
        xstart=minc-0.1*xsize
        xstop=maxc+0.1*xsize
        cc=np.linspace(minc, maxc, 100)
        for sample in self.samples.values():
            plt1=sample.approximation.fitPlot(self.concentrations,sample.meanActivities())
            plt1.show()
        plt.close()
        for sample in self.samples.values():
            plt.plot(cc, sample.approximation.eval(cc),'-',self.concentrations,sample.meanActivities(),'o')
        plt.xlim((xstart, xstop))
        #plt.title('Least-squares {} fit, R^2={:.3f}'.format(self.name,self.rsquared))
        #plt.legend([self.name+' fit', 'Reference'], loc='upper left')
        #params = ascii_uppercase[:len(self.p)]
        #ycor = max(y)
        #ystep = (ycor-min(y))/8
        #for i, (param, est) in enumerate(zip(params, self.p)):
         #   plt.text(minx, ycor*0.8-i*ystep, 'est({}) = {:.3f}'.format(param, est))
        return plt
              
    def initTestData(self):
        self.setConcentrations([10, 3.333333333, 1.111111111, 0.37037037, 0.12345679, 0.041152263, 0.013717421, 0])
        control = Sample('Control', [
            [3478, 3617, 3336, 2865, 1236, 425, 172, 150],
            [3810, 3557, 3294, 2917, 1250, 449, 192, 57],
            [4083, 4055, 3534, 2708, 1169, 620, 226, 84]])
        self.addSample(control)
        self.setReference(control.name)
        exp1 = Sample('Experiment 1', [
            [5000, 4176,3822,2106,743,296,154,94],
            [3944,3657,2972,1935,801,254,142,84],
            [4083,3886,3402,2116,677,241,136,77]])
        self.addSample(exp1)
        exp2 = Sample('Experiment 2', [
            [4250,3955,3148,1732,529,206,144,76],
            [4049,3876,3211,1719,549,189,113,64],
            [4489,4195,3306,1917,594,223,124,87]])
        self.addSample(exp2)
        
        
    

        

        