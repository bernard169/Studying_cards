import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import warning_username as warning_ui
import threading

class MyWarningUserName(warning_ui.Ui_warningUsername):
    def setupUi(self, warningUsername):
        threading.stack_size(1228800) #multiple of 4kB
        self.__choice = False
        self.dialog = warningUsername
        super().setupUi(warningUsername)
        self.yesButton.clicked.connect(self.accept)
        self.noButton.clicked.connect(self.reject)

    def accept(self):
        self.__choice = True
        self.dialog.accept()
    
    def reject(self):
        self.dialog.reject()

    def getChoice(self):
        return self.__choice