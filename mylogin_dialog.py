import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import login_dialog as login

class MyLoginDialog(login.Ui_Dialog):
    def setupUi(self, Dialog):
        self.userName = ""
        super().setupUi(Dialog)

#Begin functionalities here
        self.okButton.clicked.connect(self.okButtonClicked)
        #self.userNameInput.enterEvent.connect(self.setUserName)
        self.cancelButton.clicked.connect  (self.cancelButtonClicked)

    def setUserName(self):
        self.userName = self.userNameInput.text()
        print(self.userName)

    def okButtonClicked(self):
        self.setUserName()
        sys.exit()

    def cancelButtonClicked(self):
        sys.exit()

    def getUserName(self):
        return self.userName