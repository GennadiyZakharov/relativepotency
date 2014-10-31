'''
Created on Oct 30, 2014

@author: gzakharov
'''
from PyQt4 import QtCore, QtGui

from rpcore.experiment import Experiment
from rpcore.actions import createAction

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
        self.experiment.signalConcentrationsChanged.connect(self.concentrationsChanged)
        self.experiment.signalSampleAdded.connect(self.sampleAdded)
        
        self.dataTable=QtGui.QTableWidget()
        self.dataTable.setColumnCount(1)
        self.dataTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.dataTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.dataTable.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #self.itemDoubleClicked.connect(self.editWell)
        
        
        plotExperimentAction = createAction(self, 'Plot experiment', '',
                                          'document-open', '')
        plotExperimentAction.triggered.connect(self.plotExperiment)
        saveReferenceAction = createAction(self, 'Save reference...', '',
                                          'document-save', '')
        #saveReferenceAction.triggered.connect(self.saveReference)
        self.actionList = [plotExperimentAction,]
        
        self.headers = ['Conc']
        self.dataTable.setHorizontalHeaderLabels(self.headers)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.dataTable)
        self.setLayout(layout)
        
        QtCore.QTimer.singleShot(0, self.experiment.initTestData)
        
    
    @QtCore.pyqtSlot(object)
    def concentrationsChanged(self, concentrations):
        self.dataTable.setRowCount(len(concentrations))
        
        for i in range(len(concentrations)) :
            self.dataTable.setItem(i,0,QtGui.QTableWidgetItem('{:.3f}'.format(concentrations[i])))
        
    def sampleAdded(self, sample):
        for i,dataset in enumerate(sample.activities) :
            self.headers.append(sample.name+':'+str(i))
            column=self.dataTable.columnCount()
            self.dataTable.setColumnCount(column+1)
            for j,act in enumerate(dataset) :
                self.dataTable.setItem(j,column,QtGui.QTableWidgetItem('{:.2f}'.format(act))) 
        self.dataTable.setHorizontalHeaderLabels(self.headers)
        
    def plotExperiment(self):
        plot=self.experiment.plot()
        plot.show()