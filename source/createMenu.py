# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\Studying_cards\createMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createPageDialog(object):
    def setupUi(self, createPageDialog):
        createPageDialog.setObjectName("createPageDialog")
        createPageDialog.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        createPageDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/createButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        createPageDialog.setWindowIcon(icon)
        createPageDialog.setStyleSheet("QDialog{\n"
"background-color :qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.905028 rgba(200, 190, 255, 255));} \n"
"")
        self.coursesView = QtWidgets.QTreeWidget(createPageDialog)
        self.coursesView.setGeometry(QtCore.QRect(130, 70, 611, 371))
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
        self.addCourseButton = QtWidgets.QPushButton(createPageDialog)
        self.addCourseButton.setGeometry(QtCore.QRect(830, 100, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.addCourseButton.setFont(font)
        self.addCourseButton.setStyleSheet("QPushButton{\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/createButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addCourseButton.setIcon(icon1)
        self.addCourseButton.setObjectName("addCourseButton")
        self.addChapterButton = QtWidgets.QPushButton(createPageDialog)
        self.addChapterButton.setGeometry(QtCore.QRect(830, 150, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.addChapterButton.setFont(font)
        self.addChapterButton.setStyleSheet("QPushButton{\n"
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
        self.addChapterButton.setIcon(icon1)
        self.addChapterButton.setObjectName("addChapterButton")
        self.addCardButton = QtWidgets.QPushButton(createPageDialog)
        self.addCardButton.setGeometry(QtCore.QRect(830, 200, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.addCardButton.setFont(font)
        self.addCardButton.setStyleSheet("QPushButton{\n"
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
        self.addCardButton.setIcon(icon1)
        self.addCardButton.setObjectName("addCardButton")
        self.homeButton = QtWidgets.QPushButton(createPageDialog)
        self.homeButton.setGeometry(QtCore.QRect(830, 500, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.homeButton.setIcon(icon2)
        self.homeButton.setObjectName("homeButton")
        self.removeCourseButton = QtWidgets.QPushButton(createPageDialog)
        self.removeCourseButton.setGeometry(QtCore.QRect(830, 300, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.removeCourseButton.setFont(font)
        self.removeCourseButton.setStyleSheet("QPushButton{\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.removeCourseButton.setIcon(icon3)
        self.removeCourseButton.setObjectName("removeCourseButton")
        self.removeChapterButton = QtWidgets.QPushButton(createPageDialog)
        self.removeChapterButton.setGeometry(QtCore.QRect(830, 350, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.removeChapterButton.setFont(font)
        self.removeChapterButton.setStyleSheet("QPushButton{\n"
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
        self.removeChapterButton.setIcon(icon3)
        self.removeChapterButton.setObjectName("removeChapterButton")
        self.editButton = QtWidgets.QPushButton(createPageDialog)
        self.editButton.setGeometry(QtCore.QRect(375, 495, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.editButton.setIcon(icon4)
        self.editButton.setObjectName("editButton")
        self.previewButton = QtWidgets.QPushButton(createPageDialog)
        self.previewButton.setGeometry(QtCore.QRect(830, 450, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.previewButton.setFont(font)
        self.previewButton.setStyleSheet("QPushButton{\n"
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
        icon5.addPixmap(QtGui.QPixmap("images/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.previewButton.setIcon(icon5)
        self.previewButton.setObjectName("previewButton")

        self.retranslateUi(createPageDialog)
        QtCore.QMetaObject.connectSlotsByName(createPageDialog)

    def retranslateUi(self, createPageDialog):
        _translate = QtCore.QCoreApplication.translate
        createPageDialog.setWindowTitle(_translate("createPageDialog", "Modifier le contenu"))
        self.addCourseButton.setText(_translate("createPageDialog", " Cours"))
        self.addChapterButton.setText(_translate("createPageDialog", " Chapitre"))
        self.addCardButton.setText(_translate("createPageDialog", " Carte"))
        self.homeButton.setText(_translate("createPageDialog", "Home"))
        self.removeCourseButton.setText(_translate("createPageDialog", " Cours"))
        self.removeChapterButton.setText(_translate("createPageDialog", " Chapitre"))
        self.editButton.setText(_translate("createPageDialog", "Modifier"))
        self.previewButton.setText(_translate("createPageDialog", " Aperçu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createPageDialog = QtWidgets.QDialog()
    ui = Ui_createPageDialog()
    ui.setupUi(createPageDialog)
    createPageDialog.show()
    sys.exit(app.exec_())
