# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\source\studyMode.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_studyModeDialog(object):
    def setupUi(self, studyModeDialog):
        studyModeDialog.setObjectName("studyModeDialog")
        studyModeDialog.resize(800, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        studyModeDialog.setWindowIcon(icon)
        studyModeDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        studyModeDialog.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.gridLayout = QtWidgets.QGridLayout(studyModeDialog)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.editButton = QtWidgets.QPushButton(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setMinimumSize(QtCore.QSize(0, 50))
        self.editButton.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
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
        self.editButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon1)
        self.editButton.setIconSize(QtCore.QSize(25, 25))
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 2, 0, 1, 1)
        self.chapterLabel = QtWidgets.QLabel(studyModeDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.chapterLabel.setFont(font)
        self.chapterLabel.setObjectName("chapterLabel")
        self.gridLayout.addWidget(self.chapterLabel, 0, 0, 1, 2)
        self.validateChangeButton = QtWidgets.QPushButton(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateChangeButton.sizePolicy().hasHeightForWidth())
        self.validateChangeButton.setSizePolicy(sizePolicy)
        self.validateChangeButton.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
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
        self.validateChangeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/transparent-check-right-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.validateChangeButton.setIcon(icon2)
        self.validateChangeButton.setIconSize(QtCore.QSize(30, 30))
        self.validateChangeButton.setObjectName("validateChangeButton")
        self.gridLayout.addWidget(self.validateChangeButton, 4, 0, 1, 1)
        self.displayQA = QtWidgets.QTextEdit(studyModeDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.displayQA.setFont(font)
        self.displayQA.setStyleSheet("QTextEdit{\n"
"background-color: transparent; \n"
"}")
        self.displayQA.setReadOnly(True)
        self.displayQA.setObjectName("displayQA")
        self.gridLayout.addWidget(self.displayQA, 1, 1, 6, 3)
        self.cancelChangeButton = QtWidgets.QPushButton(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelChangeButton.sizePolicy().hasHeightForWidth())
        self.cancelChangeButton.setSizePolicy(sizePolicy)
        self.cancelChangeButton.setMaximumSize(QtCore.QSize(50, 50))
        self.cancelChangeButton.setStyleSheet("QPushButton{\n"
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
        self.cancelChangeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelChangeButton.setIcon(icon3)
        self.cancelChangeButton.setIconSize(QtCore.QSize(25, 25))
        self.cancelChangeButton.setObjectName("cancelChangeButton")
        self.gridLayout.addWidget(self.cancelChangeButton, 5, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("QPushButton{\n"
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
        self.stopButton.setIcon(icon3)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 0, 3, 1, 1)
        self.counterLabel = QtWidgets.QLabel(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.counterLabel.sizePolicy().hasHeightForWidth())
        self.counterLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.counterLabel.setFont(font)
        self.counterLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.counterLabel.setObjectName("counterLabel")
        self.gridLayout.addWidget(self.counterLabel, 1, 0, 1, 1)
        self.validateQButton = QtWidgets.QPushButton(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateQButton.sizePolicy().hasHeightForWidth())
        self.validateQButton.setSizePolicy(sizePolicy)
        self.validateQButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.validateQButton.setFont(font)
        self.validateQButton.setStyleSheet("QPushButton{\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/happySmile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.validateQButton.setIcon(icon4)
        self.validateQButton.setObjectName("validateQButton")
        self.gridLayout.addWidget(self.validateQButton, 7, 1, 1, 1)
        self.needWorkButton = QtWidgets.QPushButton(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.needWorkButton.sizePolicy().hasHeightForWidth())
        self.needWorkButton.setSizePolicy(sizePolicy)
        self.needWorkButton.setMinimumSize(QtCore.QSize(200, 0))
        self.needWorkButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.needWorkButton.setFont(font)
        self.needWorkButton.setStyleSheet("QPushButton{\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/sadSmiley.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.needWorkButton.setIcon(icon5)
        self.needWorkButton.setObjectName("needWorkButton")
        self.gridLayout.addWidget(self.needWorkButton, 7, 2, 1, 1)
        self.viewAnswerButton = QtWidgets.QPushButton(studyModeDialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.viewAnswerButton.setFont(font)
        self.viewAnswerButton.setStyleSheet("QPushButton{\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/MGlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewAnswerButton.setIcon(icon6)
        self.viewAnswerButton.setObjectName("viewAnswerButton")
        self.gridLayout.addWidget(self.viewAnswerButton, 7, 3, 1, 1)
        self.formatMenu = QtWidgets.QComboBox(studyModeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatMenu.sizePolicy().hasHeightForWidth())
        self.formatMenu.setSizePolicy(sizePolicy)
        self.formatMenu.setMaximumSize(QtCore.QSize(50, 25))
        self.formatMenu.setObjectName("formatMenu")
        self.formatMenu.addItem("")
        self.formatMenu.setItemText(0, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon7, "")
        self.formatMenu.setItemText(1, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon8, "")
        self.formatMenu.setItemText(2, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon9, "")
        self.formatMenu.setItemText(3, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/strikeOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon10, "")
        self.formatMenu.setItemText(4, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/highlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon11, "")
        self.formatMenu.setItemText(5, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/redSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon12, "")
        self.formatMenu.setItemText(6, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/greenSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon13, "")
        self.formatMenu.setItemText(7, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/purpleSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.formatMenu.addItem(icon14, "")
        self.formatMenu.setItemText(8, "")
        self.gridLayout.addWidget(self.formatMenu, 3, 0, 1, 1)

        self.retranslateUi(studyModeDialog)
        QtCore.QMetaObject.connectSlotsByName(studyModeDialog)

    def retranslateUi(self, studyModeDialog):
        _translate = QtCore.QCoreApplication.translate
        studyModeDialog.setWindowTitle(_translate("studyModeDialog", "Etude"))
        self.chapterLabel.setText(_translate("studyModeDialog", "Chapitre"))
        self.displayQA.setHtml(_translate("studyModeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">Question</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.stopButton.setText(_translate("studyModeDialog", "Arrêter"))
        self.counterLabel.setText(_translate("studyModeDialog", "1/12"))
        self.validateQButton.setText(_translate("studyModeDialog", "Valider"))
        self.needWorkButton.setText(_translate("studyModeDialog", "A revoir"))
        self.viewAnswerButton.setText(_translate("studyModeDialog", "Voir réponse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studyModeDialog = QtWidgets.QDialog()
    ui = Ui_studyModeDialog()
    ui.setupUi(studyModeDialog)
    studyModeDialog.show()
    sys.exit(app.exec_())
