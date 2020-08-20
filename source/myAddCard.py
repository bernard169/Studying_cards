from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
import utils
from addCard import Ui_selectCardType
import threading

class MyAddCardDialog(Ui_selectCardType):
    def setupUi(self, Dialog, chapter):
        threading.stack_size(1228800) #multiple of 4kB
        super().setupUi(Dialog)
        self.__dialog = Dialog
        self.__action = ""
        self.comboBox.addItem("Classique")
        self.comboBox.addItem("Image")
        self.comboBox.addItem("A partir d'un fichier")
        self.confirmButton.clicked.connect(self.validate)
        self.cancelButton.clicked.connect(self.cancel)
        self.chapterInfo.setText("Vous ajoutez une carte \n au"+
                            " chapitre {}".format(chapter))
        self.chapterInfo.setAlignment(QtCore.Qt.AlignCenter)
        for button in self.__dialog.findChildren(QtWidgets.QPushButton):
            button.pressed.connect(lambda:utils.buttonPressed(button))
            button.released.connect(lambda:utils.buttonReleased(button))

    def validate(self):
        self.__action = self.comboBox.currentText()
        self.__dialog.accept()
    
    def cancel(self):
        self.__action = "cancel"
        self.__dialog.reject()
        
    def getAction(self):
        return self.__action