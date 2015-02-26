'''
Created on Oct 30, 2014

@author: gzakharov
'''
import numpy as np
import matplotlib.pyplot as plt
from PyQt4 import QtCore

from rpcore.sample import Sample

class Experiment(QtCore.QObject):
    '''
    This class holds data for set of samples
    '''
    signalSampleAdded = QtCore.pyqtSignal(Sample)
    signalSampleRemoved = QtCore.pyqtSignal(Sample)
    signalReferenceChanged = QtCore.pyqtSignal(str)
    plotColors=['red','orange','gold','blue','purple','brown','pink'] 
    referenceColor='darkgreen'

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(Experiment, self).__init__(parent)
        self.samples = {} # sample name as a key, and list of data in item
        self.referenceSampleName = ''
        
    def setReference(self, name):
        if name in self.samples.keys() :
            self.referenceName = name
        else :
            self.referenceName = ''
            
    def addSample(self, sample):
        self.samples[sample.name]=sample
        sample.findApproximation()
        self.signalSampleAdded.emit(sample)
              
    def plotSamples(self):
        #xsize=maxc-minc
        #xstart=minc-0.1*xsize
        #xstop=maxc+0.1*xsize
        #
        legend=[]
        for i,sample in enumerate(self.samples.values()):
            if sample.name == self.referenceName:
                color =self.referenceColor
                marker='s'
                linewidth = 2
            else:
                color=self.plotColors[i]
                marker='o'
                linewidth = 1
            plt.plot(sample.concentrations,sample.meanDensities,marker, color=color)
            cc=np.linspace(min(sample.concentrations), max(sample.concentrations), 100)
            if sample.approximation is not None:
                plt.plot(cc, sample.approximation.eval(cc),'-',linewidth = linewidth,color=color)
            
            legend += [sample.name, '']
        #plt.xlim((xstart, xstop))
        plt.title('Data fit')
        plt.legend(legend, loc='lower right')
        #plt.xscale('log')
        return plt
              
    def initTestData(self):
        concentrations = [10, 3.333333333, 1.111111111, 0.37037037, 0.12345679, 0.041152263, 0.013717421, 0]
        control = Sample('Control', concentrations, [
            [3478, 3617, 3336, 2865, 1236, 425, 172, 150],
            [3810, 3557, 3294, 2917, 1250, 449, 192, 57],
            [4083, 4055, 3534, 2708, 1169, 620, 226, 84]])
        self.addSample(control)
        self.setReference(control.name)
        exp1 = Sample('Experiment 1', concentrations, [
            [5000, 4176,3822,2106,743,296,154,94],
            [3944,3657,2972,1935,801,254,142,84],
            [4083,3886,3402,2116,677,241,136,77]])
        self.addSample(exp1)
        exp2 = Sample('Experiment 2', concentrations, [
            [4250,3955,3148,1732,529,206,144,76],
            [4049,3876,3211,1719,549,189,113,64],
            [4489,4195,3306,1917,594,223,124,87]])
        self.addSample(exp2)
        
        
    

        

        