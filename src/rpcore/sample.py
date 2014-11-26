'''
Created on Oct 30, 2014

@author: gzakharov
'''
from __future__ import division

import numpy as np

class Sample(object):
    '''
    This class holds data for one sample - name and activity data
    '''

    def __init__(self, name, activities):
        '''
        Constructor
        '''
        self.name=name
        self.activities=np.array(activities)
        self.replicasCount=len(self.activities)
        self.meanVector = np.empty(self.replicasCount)
        print self.meanVector
        self.meanVector.fill(1/self.replicasCount)
        self.approximation=None
        
    def meanActivities(self):
        return np.dot(self.meanVector,self.activities)
    
    def setApproximation(self, approximation):
        self.approximation = approximation

        