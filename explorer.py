# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\explorer.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QMainWindow{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(800, 100, 160, 45))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 180), stop:0.219101 rgba(193, 0, 0, 180), stop:0.41573 rgba(154, 0, 32, 180), stop:0.629213 rgba(120, 0, 0, 180), stop:0.803371 rgba(80, 0, 0, 180), stop:1 rgba(53, 0, 0, 180));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.loginButton.setIcon(icon1)
        self.loginButton.setIconSize(QtCore.QSize(30, 30))
        self.loginButton.setObjectName("loginButton")
        self.createButton = QtWidgets.QPushButton(Dialog)
        self.createButton.setGeometry(QtCore.QRect(800, 220, 160, 45))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 255, 0, 180), stop:0.219101 rgba(0, 195, 0, 180), stop:0.41573 rgba(0, 165, 32, 180), stop:0.629213 rgba(0, 135, 0, 180), stop:0.820225 rgba(0, 103, 0, 180), stop:1 rgba(0, 51, 0, 180));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/createButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.createButton.setIcon(icon2)
        self.createButton.setIconSize(QtCore.QSize(30, 30))
        self.createButton.setObjectName("createButton")
        self.studyButton = QtWidgets.QPushButton(Dialog)
        self.studyButton.setGeometry(QtCore.QRect(800, 340, 160, 45))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.studyButton.setFont(font)
        self.studyButton.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(94, 0, 255, 150), stop:0.219101 rgba(60, 0, 204, 150), stop:0.41573 rgba(48, 0, 184, 150), stop:0.623596 rgba(37, 0, 129, 150), stop:0.769663 rgba(28, 0, 108, 150), stop:1 rgba(10, 0, 80, 150));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/study.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.studyButton.setIcon(icon3)
        self.studyButton.setIconSize(QtCore.QSize(30, 30))
        self.studyButton.setObjectName("studyButton")
        self.coursesView = QtWidgets.QTreeWidget(Dialog)
        self.coursesView.setGeometry(QtCore.QRect(110, 80, 611, 371))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.coursesView.setFont(font)
        self.coursesView.setStyleSheet("QTreeWidget{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coursesView.setObjectName("coursesView")
        self.coursesView.headerItem().setText(0, "1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Explorateur"))
        self.loginButton.setText(_translate("Dialog", "  Log out"))
        self.createButton.setText(_translate("Dialog", "  Créer"))
        self.studyButton.setText(_translate("Dialog", "  Etudier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
