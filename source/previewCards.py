# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\source\previewCards.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_previewCardsDialog(object):
    def setupUi(self, previewCardsDialog):
        previewCardsDialog.setObjectName("previewCardsDialog")
        previewCardsDialog.resize(800, 500)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        previewCardsDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        previewCardsDialog.setWindowIcon(icon)
        previewCardsDialog.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.gridLayout = QtWidgets.QGridLayout(previewCardsDialog)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.previousButton = QtWidgets.QPushButton(previewCardsDialog)
        self.previousButton.setMinimumSize(QtCore.QSize(0, 20))
        self.previousButton.setStyleSheet("QPushButton{\n"
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
        self.previousButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon1)
        self.previousButton.setObjectName("previousButton")
        self.gridLayout.addWidget(self.previousButton, 16, 2, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 8, 5, 1, 1)
        self.editButton = QtWidgets.QPushButton(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("QPushButton{\n"
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
        icon3.addPixmap(QtGui.QPixmap("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon3)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 4, 5, 1, 1)
        self.nextButton = QtWidgets.QPushButton(previewCardsDialog)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 20))
        self.nextButton.setStyleSheet("QPushButton{\n"
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
        self.nextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/arrow-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 16, 3, 1, 1)
        self.answerLabel = QtWidgets.QLabel(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.answerLabel.setFont(font)
        self.answerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLabel.setObjectName("answerLabel")
        self.gridLayout.addWidget(self.answerLabel, 13, 1, 1, 3)
        self.validateChangeButton = QtWidgets.QPushButton(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.validateChangeButton.setFont(font)
        self.validateChangeButton.setStyleSheet("QPushButton{\n"
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
        self.validateChangeButton.setIcon(icon3)
        self.validateChangeButton.setObjectName("validateChangeButton")
        self.gridLayout.addWidget(self.validateChangeButton, 15, 5, 1, 1)
        self.insertButton = QtWidgets.QPushButton(previewCardsDialog)
        self.insertButton.setMinimumSize(QtCore.QSize(0, 26))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.insertButton.setFont(font)
        self.insertButton.setStyleSheet("QPushButton{\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/createButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insertButton.setIcon(icon5)
        self.insertButton.setObjectName("insertButton")
        self.gridLayout.addWidget(self.insertButton, 13, 5, 2, 1)
        self.displayChapter = QtWidgets.QLabel(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.displayChapter.setFont(font)
        self.displayChapter.setObjectName("displayChapter")
        self.gridLayout.addWidget(self.displayChapter, 2, 0, 1, 1)
        self.questionLabel = QtWidgets.QLabel(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.questionLabel.setFont(font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName("questionLabel")
        self.gridLayout.addWidget(self.questionLabel, 4, 1, 1, 3)
        self.displayAnswer = QtWidgets.QTextEdit(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.displayAnswer.setFont(font)
        self.displayAnswer.setStyleSheet("QTextEdit{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"}")
        self.displayAnswer.setReadOnly(True)
        self.displayAnswer.setObjectName("displayAnswer")
        self.gridLayout.addWidget(self.displayAnswer, 14, 0, 1, 5)
        self.displayQuestion = QtWidgets.QTextEdit(previewCardsDialog)
        self.displayQuestion.setMaximumSize(QtCore.QSize(16777215, 138))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.displayQuestion.setFont(font)
        self.displayQuestion.setStyleSheet("QTextEdit{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"}")
        self.displayQuestion.setReadOnly(True)
        self.displayQuestion.setObjectName("displayQuestion")
        self.gridLayout.addWidget(self.displayQuestion, 8, 0, 1, 5)
        self.stopButton = QtWidgets.QPushButton(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.219101 rgba(0, 0, 204, 255), stop:0.41573 rgba(0, 0, 184, 255), stop:0.623596 rgba(0, 0, 129, 255), stop:0.769663 rgba(0, 0, 108, 255), stop:1 rgba(0, 0, 80, 255));\n"
"color:white;\n"
"border: 1px solid gray; \n"
"border-radius: 8px; \n"
"padding: 0 8px; \n"
"selection-background-color: darkgray; }\n"
"\n"
"QPushButton:Pressed{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 143, 255), stop:0.219101 rgba(0, 0, 135, 255), stop:0.41573 rgba(0, 0, 110, 255), stop:0.621762 rgba(0, 0, 92, 255), stop:0.769663 rgba(0, 0, 81, 255), stop:1 rgba(0, 0, 45, 255));\n"
"}")
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 16, 5, 1, 1)
        self.displayCounter = QtWidgets.QLabel(previewCardsDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.displayCounter.setFont(font)
        self.displayCounter.setObjectName("displayCounter")
        self.gridLayout.addWidget(self.displayCounter, 0, 0, 2, 1)
        self.formatMenuQ = QtWidgets.QComboBox(previewCardsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatMenuQ.sizePolicy().hasHeightForWidth())
        self.formatMenuQ.setSizePolicy(sizePolicy)
        self.formatMenuQ.setMaximumSize(QtCore.QSize(70, 16777215))
        self.formatMenuQ.setObjectName("formatMenuQ")
        self.formatMenuQ.addItem("")
        self.formatMenuQ.setItemText(0, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon6, "")
        self.formatMenuQ.setItemText(1, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon7, "")
        self.formatMenuQ.setItemText(2, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon8, "")
        self.formatMenuQ.setItemText(3, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/strikeOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon9, "")
        self.formatMenuQ.setItemText(4, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/redSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon10, "")
        self.formatMenuQ.setItemText(5, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/greenSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenuQ.addItem(icon11, "")
        self.formatMenuQ.setItemText(6, "")
        self.gridLayout.addWidget(self.formatMenuQ, 2, 5, 1, 1)
        self.formatMenuA = QtWidgets.QComboBox(previewCardsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatMenuA.sizePolicy().hasHeightForWidth())
        self.formatMenuA.setSizePolicy(sizePolicy)
        self.formatMenuA.setMaximumSize(QtCore.QSize(70, 16777215))
        self.formatMenuA.setObjectName("formatMenuA")
        self.formatMenuA.addItem("")
        self.formatMenuA.setItemText(0, "")
        self.formatMenuA.addItem(icon6, "")
        self.formatMenuA.setItemText(1, "")
        self.formatMenuA.addItem(icon7, "")
        self.formatMenuA.setItemText(2, "")
        self.formatMenuA.addItem(icon8, "")
        self.formatMenuA.setItemText(3, "")
        self.formatMenuA.addItem(icon9, "")
        self.formatMenuA.setItemText(4, "")
        self.formatMenuA.addItem(icon10, "")
        self.formatMenuA.setItemText(5, "")
        self.formatMenuA.addItem(icon11, "")
        self.formatMenuA.setItemText(6, "")
        self.gridLayout.addWidget(self.formatMenuA, 9, 5, 1, 1)

        self.retranslateUi(previewCardsDialog)
        QtCore.QMetaObject.connectSlotsByName(previewCardsDialog)

    def retranslateUi(self, previewCardsDialog):
        _translate = QtCore.QCoreApplication.translate
        previewCardsDialog.setWindowTitle(_translate("previewCardsDialog", "Preview"))
        self.deleteButton.setText(_translate("previewCardsDialog", "Supprimer"))
        self.editButton.setText(_translate("previewCardsDialog", "Modifier"))
        self.answerLabel.setText(_translate("previewCardsDialog", "Réponse : "))
        self.validateChangeButton.setText(_translate("previewCardsDialog", "Confirmer"))
        self.insertButton.setText(_translate("previewCardsDialog", "Insérer"))
        self.displayChapter.setText(_translate("previewCardsDialog", "Chapitre"))
        self.questionLabel.setText(_translate("previewCardsDialog", "Question :"))
        self.stopButton.setText(_translate("previewCardsDialog", "Arrêter"))
        self.displayCounter.setText(_translate("previewCardsDialog", "1/12"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    previewCardsDialog = QtWidgets.QDialog()
    ui = Ui_previewCardsDialog()
    ui.setupUi(previewCardsDialog)
    previewCardsDialog.show()
    sys.exit(app.exec_())
