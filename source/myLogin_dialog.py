import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import login_dialog as login
import utils
import threading

class MyLoginDialog(login.Ui_Dialog):
    def setupUi(self, Dialog):
        threading.stack_size(1228800) #multiple of 4kB
        self.userName = ""
        self.dialog = Dialog
        super().setupUi(Dialog)
        #Begin functionalities here
        self.okButton.pressed.connect(lambda:utils.buttonPressed(self.okButton))
        self.okButton.released.connect(lambda:utils.buttonReleased(self.okButton))
        self.okButton.clicked.connect(self.validate)
        #self.userNameInput.enterEvent.connect(self.setUserName)
        self.cancelButton.pressed.connect(lambda:utils.buttonPressed(self.cancelButton))
        self.cancelButton.released.connect(lambda:utils.buttonReleased(self.cancelButton))
        self.cancelButton.clicked.connect  (self.cancel)

    def setUserName(self):
        self.userName = self.userNameInput.text()

    def validate(self):
        self.setUserName()
        self.dialog.accept()

    def cancel(self):
        self.dialog.reject()

    def getUserName(self):
        return self.userName