from chooseStudyStyle import Ui_Dialog as chStStDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class myChooseStudyStyleDialog(chStStDialog):
    def setupUi(self, dialog):
        super().setupUi(dialog)
        self.__dialog = dialog
        self.__choice = ""
        self.orderedButton.clicked.connect(self.chooseOrder)
        self.randomButton.clicked.connect(self.chooseRandom)
    
    def chooseOrder(self):
        self.__choice = "ordered"
        self.__dialog.accept()

    def chooseRandom(self):
        self.__choice = "random"
        self.__dialog.accept()

    def getInfos(self):
        return self.__choice