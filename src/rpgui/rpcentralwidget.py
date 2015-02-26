'''
Created on Oct 30, 2014

@author: gzakharov
'''
from PyQt4 import QtCore, QtGui

from rpcore.experiment import Experiment
from rpcore.actions import createAction
from rpgui.plotwidget import PlotWidget

class RpCentralWidget(QtGui.QWidget):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(RpCentralWidget, self).__init__(parent)
        self.setObjectName("rpCentralWidget")
        
        self.experiment = Experiment(self)
        self.experiment.signalSampleAdded.connect(self.sampleAdded)
        
        self.dataTable=QtGui.QTableWidget()
        self.dataTable.setColumnCount(1)
        self.dataTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.dataTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.dataTable.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        
        self.plotWidget = PlotWidget(self)
        
        
        
        plotExperimentAction = createAction(self, 'Plot experiment', '',
                                          'document-open', '')
        plotExperimentAction.triggered.connect(self.plotExperiment)
        saveReferenceAction = createAction(self, 'Save reference...', '',
                                          'document-save', '')
        #saveReferenceAction.triggered.connect(self.saveReference)
        self.actionList = [plotExperimentAction,]
        
        self.headers = ['Conc']
        self.dataTable.setHorizontalHeaderLabels(self.headers)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.dataTable)
        layout.addWidget(self.plotWidget)
        self.setLayout(layout)
        
        QtCore.QTimer.singleShot(0, self.experiment.initTestData)
        
        
        
    
    def sampleAdded(self, sample):
        self.dataTable.setRowCount(len(sample.concentrations))
        for i,concenration in enumerate( sample.concentrations ):
            self.dataTable.setItem(i,0,QtGui.QTableWidgetItem('{:.2f}'.format(concenration)))
        for i,dataset in enumerate(sample.densities) :
            self.headers.append(sample.name+':'+str(i))
            column=self.dataTable.columnCount()
            self.dataTable.setColumnCount(column+1)
            for j,density in enumerate(dataset) :
                self.dataTable.setItem(j,column,QtGui.QTableWidgetItem('{:.2f}'.format(density))) 
        self.dataTable.setHorizontalHeaderLabels(self.headers)
        
    def plotExperiment(self):
        plot=self.experiment.plotSamples()
        plot.show()