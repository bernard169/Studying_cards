# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\addStructuralItemDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateStructure(object):
    def setupUi(self, CreateStructure):
        CreateStructure.setObjectName("CreateStructure")
        CreateStructure.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        CreateStructure.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/createButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreateStructure.setWindowIcon(icon)
        CreateStructure.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.confirm = QtWidgets.QPushButton(CreateStructure)
        self.confirm.setGeometry(QtCore.QRect(53, 210, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(185, 132, 255, 255), stop:0.212435 rgba(156, 105, 204, 255), stop:0.41573 rgba(157, 95, 184, 255), stop:0.623596 rgba(134, 67, 136, 255), stop:0.766839 rgba(118, 59, 125, 255), stop:1 rgba(104, 61, 99, 255));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }\n"
"\n"
"QPushButton:pressed{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(104, 74, 143, 255), stop:0.212435 rgba(99, 67, 130, 255), stop:0.41573 rgba(97, 58, 114, 255), stop:0.621762 rgba(90, 47, 91, 255), stop:0.766839 rgba(87, 43, 92, 255), stop:1 rgba(68, 40, 65, 255));\n"
"}")
        self.confirm.setObjectName("confirm")
        self.Cancel = QtWidgets.QPushButton(CreateStructure)
        self.Cancel.setGeometry(QtCore.QRect(226, 210, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(185, 132, 255, 255), stop:0.212435 rgba(156, 105, 204, 255), stop:0.41573 rgba(157, 95, 184, 255), stop:0.623596 rgba(134, 67, 136, 255), stop:0.766839 rgba(118, 59, 125, 255), stop:1 rgba(104, 61, 99, 255));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }\n"
"\n"
"QPushButton:pressed{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(104, 74, 143, 255), stop:0.212435 rgba(99, 67, 130, 255), stop:0.41573 rgba(97, 58, 114, 255), stop:0.621762 rgba(90, 47, 91, 255), stop:0.766839 rgba(87, 43, 92, 255), stop:1 rgba(68, 40, 65, 255));\n"
"}")
        self.Cancel.setObjectName("Cancel")
        self.order = QtWidgets.QLabel(CreateStructure)
        self.order.setGeometry(QtCore.QRect(50, 40, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.order.setFont(font)
        self.order.setObjectName("order")
        self.nameInput = QtWidgets.QLineEdit(CreateStructure)
        self.nameInput.setGeometry(QtCore.QRect(75, 125, 250, 24))
        self.nameInput.setStyleSheet("QLineEdit {border: 2px solid gray; \n"
"border-radius: 10px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.nameInput.setObjectName("nameInput")

        self.retranslateUi(CreateStructure)
        QtCore.QMetaObject.connectSlotsByName(CreateStructure)

    def retranslateUi(self, CreateStructure):
        _translate = QtCore.QCoreApplication.translate
        CreateStructure.setWindowTitle(_translate("CreateStructure", "Ajouter un élément"))
        self.confirm.setText(_translate("CreateStructure", "Valider"))
        self.Cancel.setText(_translate("CreateStructure", "Annuler"))
        self.order.setText(_translate("CreateStructure", "Entrez le nom de chapitre désiré :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateStructure = QtWidgets.QDialog()
    ui = Ui_CreateStructure()
    ui.setupUi(CreateStructure)
    CreateStructure.show()
    sys.exit(app.exec_())
