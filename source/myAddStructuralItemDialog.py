from PyQt5 import QtCore, QtGui, QtWidgets
from addStructuralItemDialog import Ui_CreateStructure
import threading

class MyAddStructuralItemDialog(Ui_CreateStructure):
    def setupUi(self, Dialog):
        threading.stack_size(1228800) #multiple of 4kB
        super().setupUi(Dialog)
        self.__action = ""
        self.__dialog = Dialog
        self.__name = ""
        self.confirm.clicked.connect(self.confirmButton)
        self.Cancel.clicked.connect(self.cancelButton)
        
    def getInfos(self):
        return self.__action, self.__name

    def confirmButton(self):
        self.__action = "confirm"
        self.__name = self.nameInput.text()
        self.__dialog.accept()

    def cancelButton(self):
        self.__action = "cancel"
        self.__dialog.reject()

    def setContent(self, context):
        _translate = QtCore.QCoreApplication.translate
        if context == "edit":
            self.order.setText(_translate("CreateStructure", 
            "Entrez le nouveau nom désiré :"))
        elif context == "editQuestion" : 
            self.order.setText(_translate("CreateStructure", 
            "Entrez la nouvelle question désirée :"))
        elif context == "editAnswer" :
            self.order.setText(_translate("CreateStructure", 
            "Entrez la nouvelle réponse désirée :"))
        else :
            self.order.setText(_translate("CreateStructure", 
            "Entrez le nom de {} désiré :".format(context)))
        
