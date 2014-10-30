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
        self.approximation=None
        
    def meanActivities(self):
        return np.dot(np.array([1/3,1/3,1/3]),self.activities)
    
    def setApproximation(self, approximation):
        self.approximation = approximation

        