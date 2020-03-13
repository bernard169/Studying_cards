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
        Dialog.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(800, 100, 160, 45))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 120, 120, 255), stop:0.217617 rgba(204, 96, 96, 255), stop:0.41573 rgba(184, 85, 85, 255), stop:0.623596 rgba(129, 61, 61, 255), stop:0.769663 rgba(108, 43, 43, 255), stop:1 rgba(80, 39, 39, 255));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }\n"
"\n"
"QPushButton:Pressed{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(151, 71, 71, 255), stop:0.217617 rgba(138, 65, 65, 255), stop:0.41573 rgba(127, 58, 58, 255), stop:0.623596 rgba(102, 48, 48, 255), stop:0.769663 rgba(92, 37, 37, 255), stop:1 rgba(71, 34, 34, 255));\n"
"}\n"
"")
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
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(120, 255, 170, 255), stop:0.217617 rgba(96, 204, 103, 255), stop:0.41573 rgba(94, 184, 85, 255), stop:0.623596 rgba(64, 129, 61, 255), stop:0.769663 rgba(43, 108, 44, 255), stop:1 rgba(39, 80, 41, 255));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }\n"
"\n"
"QPushButton:Pressed{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(65, 138, 92, 255), stop:0.217617 rgba(60, 128, 64, 255), stop:0.41573 rgba(59, 115, 53, 255), stop:0.623596 rgba(44, 89, 42, 255), stop:0.769663 rgba(29, 75, 31, 255), stop:1 rgba(27, 55, 28, 255));\n"
"}")
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
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 4px; \n"
"selection-background-color: darkgray;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-radius: 8px; \n"
"    /*padding-left: 0 8px;*/\n"
"    border: 1px solid transparent;\n"
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
