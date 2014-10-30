'''
Created on 01.11.2013

@author: gena
'''
from PyQt4 import QtCore, QtGui


from rpcore.consts import applicationName,applicationVersion
import imagercc

class RpMainWindow(QtGui.QMainWindow):
    '''
    Main window for elisaSolver
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(RpMainWindow, self).__init__(parent)
        self.setObjectName("rpMainWindow") 
        self.setWindowTitle(applicationName+' '+str(applicationVersion))
        #
                
        
        #self.setCentralWidget(mainWindow)
        #
        
    '''
    def closeEvent(self, event):
        # Asking user to confirm
        reply = self.plateManagerWidget.closeAllPlates()
        if reply == QtGui.QMessageBox.Cancel :
            event.ignore()
            return
        # Save settings and exit 
        settings = QtCore.QSettings()
        settings.setValue("esMainWindow/Geometry", 
                              QtCore.QVariant(self.saveGeometry()))
        settings.setValue("esMainWindow/State", 
                              QtCore.QVariant(self.saveState()))
        settings.setValue('lastDirectory',QtCore.QVariant(self.plateManagerWidget.lastDirectory))
        settings.setValue('referenceLastDirectory',QtCore.QVariant(self.plateWidget.lastDirectory))
        settings.setValue('defaultApproximationIndex',QtCore.QVariant(self.typeComboBox.currentIndex()))
        event.accept()
    '''