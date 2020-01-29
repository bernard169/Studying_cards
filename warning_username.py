# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\warning_username.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_warningUsername(object):
    def setupUi(self, warningUsername):
        warningUsername.setObjectName("warningUsername")
        warningUsername.resize(443, 324)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/add-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        warningUsername.setWindowIcon(icon)
        warningUsername.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.label = QtWidgets.QLabel(warningUsername)
        self.label.setGeometry(QtCore.QRect(0, 150, 441, 101))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.yesButton = QtWidgets.QPushButton(warningUsername)
        self.yesButton.setGeometry(QtCore.QRect(110, 260, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.yesButton.setFont(font)
        self.yesButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(197, 198, 255);\n"
"border: 1px solid blue; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(warningUsername)
        self.noButton.setGeometry(QtCore.QRect(250, 260, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.noButton.setFont(font)
        self.noButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(197, 198, 255);\n"
"border: 1px solid blue; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.noButton.setObjectName("noButton")
        self.logoLabel = QtWidgets.QLabel(warningUsername)
        self.logoLabel.setGeometry(QtCore.QRect(0, 10, 441, 191))
        self.logoLabel.setStyleSheet("")
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("images/warning.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setObjectName("logoLabel")

        self.retranslateUi(warningUsername)
        QtCore.QMetaObject.connectSlotsByName(warningUsername)

    def retranslateUi(self, warningUsername):
        _translate = QtCore.QCoreApplication.translate
        warningUsername.setWindowTitle(_translate("warningUsername", "Créer cet utilisateur"))
        self.label.setText(_translate("warningUsername", "Le nom d\'utilisateur sélectionné n\'existe pas encore \n"
" Souhaitez-vous créer cet utilisateur ? "))
        self.yesButton.setText(_translate("warningUsername", "Oui"))
        self.noButton.setText(_translate("warningUsername", "Non"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    warningUsername = QtWidgets.QDialog()
    ui = Ui_warningUsername()
    ui.setupUi(warningUsername)
    warningUsername.show()
    sys.exit(app.exec_())
