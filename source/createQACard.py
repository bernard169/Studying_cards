# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\source\createQACard.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createQACardDialog(object):
    def setupUi(self, createQACardDialog):
        createQACardDialog.setObjectName("createQACardDialog")
        createQACardDialog.resize(800, 500)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        createQACardDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/createButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        createQACardDialog.setWindowIcon(icon)
        createQACardDialog.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.gridLayout = QtWidgets.QGridLayout(createQACardDialog)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.questionInput = QtWidgets.QTextEdit(createQACardDialog)
        self.questionInput.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.questionInput.setFont(font)
        self.questionInput.setStyleSheet("QTextEdit{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.questionInput.setObjectName("questionInput")
        self.gridLayout.addWidget(self.questionInput, 1, 0, 3, 7)
        self.answerInput = QtWidgets.QTextEdit(createQACardDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.answerInput.setFont(font)
        self.answerInput.setStyleSheet("QTextEdit{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }")
        self.answerInput.setObjectName("answerInput")
        self.gridLayout.addWidget(self.answerInput, 5, 0, 2, 7)
        self.cancelButton = QtWidgets.QPushButton(createQACardDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton{\n"
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
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 7, 5, 1, 1)
        self.confirmButton = QtWidgets.QPushButton(createQACardDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.confirmButton.setFont(font)
        self.confirmButton.setStyleSheet("QPushButton{\n"
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
        self.confirmButton.setObjectName("confirmButton")
        self.gridLayout.addWidget(self.confirmButton, 7, 3, 1, 1)
        self.newCardButton = QtWidgets.QPushButton(createQACardDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.newCardButton.setFont(font)
        self.newCardButton.setStyleSheet("QPushButton{\n"
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
        self.newCardButton.setObjectName("newCardButton")
        self.gridLayout.addWidget(self.newCardButton, 7, 1, 1, 1)
        self.labelQuestion = QtWidgets.QLabel(createQACardDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.labelQuestion.setFont(font)
        self.labelQuestion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuestion.setObjectName("labelQuestion")
        self.gridLayout.addWidget(self.labelQuestion, 0, 2, 1, 1)
        self.labelAnswer = QtWidgets.QLabel(createQACardDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.labelAnswer.setFont(font)
        self.labelAnswer.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnswer.setObjectName("labelAnswer")
        self.gridLayout.addWidget(self.labelAnswer, 4, 2, 1, 1)
        self.formatMenuQ = QtWidgets.QComboBox(createQACardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatMenuQ.sizePolicy().hasHeightForWidth())
        self.formatMenuQ.setSizePolicy(sizePolicy)
        self.formatMenuQ.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.formatMenuQ.setFont(font)
        self.formatMenuQ.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formatMenuQ.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.formatMenuQ.setObjectName("formatMenuQ")
        self.formatMenuQ.addItem("")
        self.formatMenuQ.setItemText(0, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon1, "")
        self.formatMenuQ.setItemText(1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon2, "")
        self.formatMenuQ.setItemText(2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon3, "")
        self.formatMenuQ.setItemText(3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/strikeOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon4, "")
        self.formatMenuQ.setItemText(4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/highlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon5, "")
        self.formatMenuQ.setItemText(5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/redSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon6, "")
        self.formatMenuQ.setItemText(6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/greenSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon7, "")
        self.formatMenuQ.setItemText(7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/purpleSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon8, "")
        self.formatMenuQ.setItemText(8, "")
        self.gridLayout.addWidget(self.formatMenuQ, 0, 6, 1, 1)
        self.formatMenuA = QtWidgets.QComboBox(createQACardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatMenuA.sizePolicy().hasHeightForWidth())
        self.formatMenuA.setSizePolicy(sizePolicy)
        self.formatMenuA.setMinimumSize(QtCore.QSize(0, 0))
        self.formatMenuA.setMaximumSize(QtCore.QSize(50, 16777215))
        self.formatMenuA.setObjectName("formatMenuA")
        self.formatMenuA.addItem("")
        self.formatMenuA.setItemText(0, "")
        self.formatMenuA.addItem(icon1, "")
        self.formatMenuA.setItemText(1, "")
        self.formatMenuA.addItem(icon2, "")
        self.formatMenuA.setItemText(2, "")
        self.formatMenuA.addItem(icon3, "")
        self.formatMenuA.setItemText(3, "")
        self.formatMenuA.addItem(icon4, "")
        self.formatMenuA.setItemText(4, "")
        self.formatMenuA.addItem(icon5, "")
        self.formatMenuA.setItemText(5, "")
        self.formatMenuA.addItem(icon6, "")
        self.formatMenuA.setItemText(6, "")
        self.formatMenuA.addItem(icon7, "")
        self.formatMenuA.setItemText(7, "")
        self.formatMenuA.addItem(icon8, "")
        self.formatMenuA.setItemText(8, "")
        self.gridLayout.addWidget(self.formatMenuA, 4, 6, 1, 1)

        self.retranslateUi(createQACardDialog)
        QtCore.QMetaObject.connectSlotsByName(createQACardDialog)

    def retranslateUi(self, createQACardDialog):
        _translate = QtCore.QCoreApplication.translate
        createQACardDialog.setWindowTitle(_translate("createQACardDialog", "Créer une carte"))
        self.cancelButton.setText(_translate("createQACardDialog", "Annuler"))
        self.confirmButton.setText(_translate("createQACardDialog", "Terminer"))
        self.newCardButton.setText(_translate("createQACardDialog", "Nouvelle carte"))
        self.labelQuestion.setText(_translate("createQACardDialog", "Question :"))
        self.labelAnswer.setText(_translate("createQACardDialog", "Réponse : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createQACardDialog = QtWidgets.QDialog()
    ui = Ui_createQACardDialog()
    ui.setupUi(createQACardDialog)
    createQACardDialog.show()
    sys.exit(app.exec_())
