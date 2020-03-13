# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\addCard.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selectCardType(object):
    def setupUi(self, selectCardType):
        selectCardType.setObjectName("selectCardType")
        selectCardType.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        selectCardType.setFont(font)
        selectCardType.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.comboBox = QtWidgets.QComboBox(selectCardType)
        self.comboBox.setGeometry(QtCore.QRect(110, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.confirmButton = QtWidgets.QPushButton(selectCardType)
        self.confirmButton.setGeometry(QtCore.QRect(110, 220, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.confirmButton.setFont(font)
        self.confirmButton.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(94, 0, 255, 150), stop:0.219101 rgba(60, 0, 204, 150), stop:0.41573 rgba(48, 0, 184, 150), stop:0.623596 rgba(37, 0, 129, 150), stop:0.769663 rgba(28, 0, 108, 150), stop:1 rgba(10, 0, 80, 150));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.confirmButton.setObjectName("confirmButton")
        self.chapterInfo = QtWidgets.QLabel(selectCardType)
        self.chapterInfo.setGeometry(QtCore.QRect(90, 20, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.chapterInfo.setFont(font)
        self.chapterInfo.setText("")
        self.chapterInfo.setObjectName("chapterInfo")
        self.cancelButton = QtWidgets.QPushButton(selectCardType)
        self.cancelButton.setGeometry(QtCore.QRect(230, 220, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(94, 0, 255, 150), stop:0.219101 rgba(60, 0, 204, 150), stop:0.41573 rgba(48, 0, 184, 150), stop:0.623596 rgba(37, 0, 129, 150), stop:0.769663 rgba(28, 0, 108, 150), stop:1 rgba(10, 0, 80, 150));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(selectCardType)
        QtCore.QMetaObject.connectSlotsByName(selectCardType)

    def retranslateUi(self, selectCardType):
        _translate = QtCore.QCoreApplication.translate
        selectCardType.setWindowTitle(_translate("selectCardType", "Paramètres de création"))
        self.confirmButton.setText(_translate("selectCardType", "OK"))
        self.cancelButton.setText(_translate("selectCardType", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectCardType = QtWidgets.QDialog()
    ui = Ui_selectCardType()
    ui.setupUi(selectCardType)
    selectCardType.show()
    sys.exit(app.exec_())
