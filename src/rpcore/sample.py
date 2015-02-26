'''
Created on Oct 30, 2014

@author: gzakharov
'''
from __future__ import division

import numpy as np
from rpcore.logistic4 import Logistic4

class Sample(object):
    '''
    This class holds data for one sample - name concenttration and dencity data
    '''

    def __init__(self, name, concentrations, densities):
        '''
        Constructor
        '''
        self.name=name # Sample name
        self.concentrations=np.array(concentrations) # 1D np array for concentrations
        self.densities=np.array(densities) # 2D numpy array with densities replicas
        replicasCount,measuresCount=self.densities.shape
        if measuresCount != len (self.concentrations) :
            raise
        meanVector = np.empty(replicasCount)
        meanVector.fill(1/replicasCount)
        self.meanDensities = np.dot(meanVector,self.densities)
        self.approximation=None
        
    def findApproximation(self):
        self.approximation = Logistic4(self.concentrations,self.meanDensities)
        
    
        

        