'''
Created on 26 feb. 2015.

@author: Gena
'''
from PyQt4 import QtCore, QtGui

class PlotWidget(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(PlotWidget, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        
        layout2 = QtGui.QHBoxLayout()
        layout.addLayout(layout2)
        self.setLayout(layout)
        
        
    