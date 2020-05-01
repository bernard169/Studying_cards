from chooseStudyStyle import Ui_Dialog as chStStDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class myChooseStudyStyleDialog(chStStDialog):
    def setupUi(self, dialog):
        super().setupUi(dialog)
        self.__dialog = dialog
        self.__choice = []
        self.orderedButton.clicked.connect(self.chooseOrder)
        self.randomButton.clicked.connect(self.chooseRandom)
        self.spacinginput.setMinimum(3)
        self.minPointsInput.setMinimum(1)

    def chooseOrder(self):
        self.__choice.append("ordered")
        self.__choice.append(self.spacinginput.value())
        self.__choice.append(self.minPointsInput.value())
        self.__dialog.accept()

    def chooseRandom(self):
        self.__choice.append("random")
        self.__choice.append(self.spacinginput.value())
        self.__choice.append(self.minPointsInput.value())
        self.__dialog.accept()

    def getInfos(self):
        return self.__choice