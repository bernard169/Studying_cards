from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
from createQACard import Ui_createQACardDialog
import utils

class MyCreateQACard(Ui_createQACardDialog):
    def setupUi(self, Dialog, db, course, chapter, userName):
        super().setupUi(Dialog)
        print("\n \n CHAPTER IS", chapter)
        print(chapter=="1 espace")
        if (userName == "chloé"):
            self.answerInput.selectAll()
            self.answerInput.setFontPointSize(14)
            self.questionInput.selectAll()
            self.questionInput.setFontPointSize(14)
            #self.textSlLabel.setVisible(False)
            #self.buttonSlLabel.setVisible(False)
            #self.textPoliceSlider.setVisible(False)
            #self.buttonPoliceSlider.setVisible(False)

        self.dialog = Dialog
        self.__action = ""
        self.__question = ""
        self.__answer = "" 
        self.__relPathToDatabase = db
        self.__course = course
        self.__chapter = chapter
        self.__userName = userName
        self.__formatQ = []
        self.__formatA = []
        self.confirmButton.pressed.connect(lambda: utils.buttonPressed(self.confirmButton))
        self.confirmButton.released.connect(lambda:utils.buttonReleased(self.confirmButton))
        self.confirmButton.clicked.connect(self.finish)
        self.cancelButton.pressed.connect(lambda:utils.buttonPressed(self.cancelButton))
        self.cancelButton.released.connect(lambda:utils.buttonReleased(self.cancelButton))
        self.cancelButton.clicked.connect(self.cancel)
        self.newCardButton.pressed.connect(lambda:utils.buttonPressed(self.newCardButton))
        self.newCardButton.released.connect(lambda:utils.buttonReleased(self.newCardButton))
        self.newCardButton.clicked.connect(self.newCard)
        #self.textPoliceSlider.setValue(50)
        #self.textPoliceSlider.valueChanged.connect(self.changeTextPolice)
        #self.buttonPoliceSlider.setValue(50)
        #self.buttonPoliceSlider.valueChanged.connect(self.changeButtonPolice)
        self.formatMenuQ.currentIndexChanged.connect(lambda:utils.formatText(self.formatMenuQ, self.questionInput))
        self.formatMenuA.currentIndexChanged.connect(lambda:utils.formatText(self.formatMenuA, self.answerInput))

    def getInfos(self):
        return self.__action, self.__question, self.__answer

    def confirm(self):
        self.__question = self.questionInput.toPlainText()
        self.__answer = self.answerInput.toPlainText()
        if self.__question == "" or self.__answer == "":
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Vous avez créé une carte avec un champ vide")
            msg.setIcon(QMessageBox.Warning)
            ex = msg.exec_()
            return None 
        self.__action = "confirm"

        #find all variations in format in question then answer
        self.__formatQ,  noFormatQ= utils.addFormat(self.questionInput, self.__question)
        self.__formatA, noFormatA = utils.addFormat(self.answerInput, self.__answer)

        data = None
        with open(self.__relPathToDatabase, 'r') as  jsonFile:
            database = json.load(jsonFile)
        
        for globalData in database['globalData']:
            if globalData['username'] == self.__userName:
                for course in globalData['data']['courses']: 
                    if course['name'] == self.__course :
                        print("course found")
                        for chapter in course["contentCourse"]:
                            if self.__chapter in chapter['name'] : 
                                if noFormatQ and noFormatA:
                                    chapter['contentChapter'].append(
                                        {"id" : len(chapter['contentChapter']),
                                        "contentCard" : 
                                            {"Q": self.__question,
                                            "A": self.__answer},
                                        "format" : {} 
                                        })
                                else :
                                    chapter['contentChapter'].append(
                                    {"id" : len(chapter['contentChapter']),
                                    "contentCard" : 
                                        {"Q": self.__question,
                                         "A": self.__answer},
                                    "format" : 
                                    {
                                        "Q" : self.__formatQ,
                                        "A" : self.__formatA
                                    }})

                            
                data = globalData['data']
        
        with open(self.__relPathToDatabase, 'w') as reWriteFile:
            json.dump(database, reWriteFile)

        self.__data = data

    def finish(self):
        self.confirm()
        self.dialog.accept()

    def newCard(self):
        self.confirm()
        self.questionInput.setPlainText("")
        self.answerInput.setPlainText("")

    def cancel(self):
        self.__action = "cancel"
        self.dialog.reject()

    def buttonPressed(self, widget):
        widget.resize(0.95 * widget.width(), 0.95 * widget.height())
    
    def buttonReleased(self, widget):
        widget.resize((1/0.95) * widget.width(), (1/0.95) * widget.height())
    
    def formatText(self, menu, textWidget):
        index = menu.currentIndex()
        cursor = textWidget.textCursor()#QtGui.QTextCursor()
        fmt = cursor.charFormat()
        #self.questionInput.setTextCursor(cursor)
        font = textWidget.currentFont()
        color = fmt.foreground().color()
        if index is 1 :
            font.setBold(True)
        elif index is 2:
            font.setUnderline(True)
        elif index is 3:
            font.setItalic(True)
        elif index is 4:
            font.setStrikeOut(True)
        elif index is 5 : 
            color.setNamedColor("red")
        elif index is 6 : 
            color.setNamedColor("green")
        elif index is 0 :
            color.setNamedColor("black")
            font.setBold(False)
            font.setUnderline(False)
            font.setItalic(False)
            font.setStrikeOut(False)
        brush = QtGui.QBrush(color)
        fmt.setFont(font)
        fmt.setForeground(brush)
        cursor.setCharFormat(fmt)