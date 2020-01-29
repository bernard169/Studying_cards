# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(600, 350)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(0.905028, QtGui.QColor(200, 190, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        Dialog.setPalette(palette)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Belgium))
        self.userNameInput = QtWidgets.QLineEdit(Dialog)
        self.userNameInput.setGeometry(QtCore.QRect(200, 180, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.userNameInput.setFont(font)
        self.userNameInput.setStyleSheet("QLineEdit {border: 2px solid gray; \n"
"border-radius: 10px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.userNameInput.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.userNameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameInput.setObjectName("userNameInput")
        self.label_userName = QtWidgets.QLabel(Dialog)
        self.label_userName.setGeometry(QtCore.QRect(110, 100, 491, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(5, 0, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 0, 34, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 0, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 0, 34, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 166, 168, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_userName.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(13)
        self.label_userName.setFont(font)
        self.label_userName.setObjectName("label_userName")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(200, 300, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.okButton.setFont(font)
        self.okButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(197, 198, 255);\n"
"border: 1px solid blue; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(320, 300, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(197, 198, 255);\n"
"border: 1px solid blue; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label_userName.setText(_translate("Dialog", "Veuillez entrer votre nom d\'utilisateur :"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
