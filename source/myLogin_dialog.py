import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import login_dialog as login

class MyLoginDialog(login.Ui_Dialog):
    def setupUi(self, Dialog):
        self.userName = ""
        self.dialog = Dialog
        super().setupUi(Dialog)
        #Begin functionalities here
        self.okButton.pressed.connect(lambda:self.buttonPressed(self.okButton))
        self.okButton.released.connect(lambda:self.buttonReleased(self.okButton))
        self.okButton.clicked.connect(self.validate)
        #self.userNameInput.enterEvent.connect(self.setUserName)
        self.cancelButton.pressed.connect(lambda:self.buttonPressed(self.cancelButton))
        self.cancelButton.released.connect(lambda:self.buttonReleased(self.cancelButton))
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

    def buttonPressed(self, widget):
        widget.resize(0.95 * widget.width(), 0.95 * widget.height())
    
    def buttonReleased(self, widget):
        widget.resize((1/0.95) * widget.width(), (1/0.95) * widget.height())