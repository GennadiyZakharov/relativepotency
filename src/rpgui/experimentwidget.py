'''
Created on 26 feb. 2015.

@author: Gena
'''
from PyQt4 import QtCore, QtGui

from rpcore.experiment import Experiment


class ExperimentWidget(object):
    '''
    classdocs
    '''


    def __init__(self, experiment, parent=None):
        '''
        Constructor
        '''
        super(ExperimentWidget, self).__init__(parent)
        self.experiment=experiment
        self.experiment.signalSampleAdded.connect(self.sampleAdded)
        self.samples={}
        
    def sampleAdded(self, sample):
        pass