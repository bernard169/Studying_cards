from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
from addCard import Ui_selectCardType

class MyAddCardDialog(Ui_selectCardType):
    def setupUi(self, Dialog, chapter):
        super().setupUi(Dialog)
        self.dialog = Dialog
        self.__action = ""
        self.comboBox.addItem("Classique")
        self.comboBox.addItem("Image")
        self.comboBox.addItem("A partir d'un fichier")
        self.confirmButton.clicked.connect(self.validate)
        self.chapterInfo.setText("Vous ajoutez une carte \n au"+
                            " chapitre {}".format(chapter))
        self.chapterInfo.setAlignment(QtCore.Qt.AlignCenter)

    def validate(self):
        self.__action = self.comboBox.currentText()
        self.dialog.accept()
    
    def cancel(self):
        self.__action = "cancel"
        self.dialog.reject()
        
    def getAction(self):
        return self.__action