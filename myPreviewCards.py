import os
import sys
import json
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from previewCards import Ui_previewCardsDialog
from myAddStructuralItemDialog import MyAddStructuralItemDialog

class MyPreviewCards(Ui_previewCardsDialog):
    def setupUi(self, Dialog, data, databaseFile, course, userName, chapter = None):
        super().setupUi(Dialog)
        #self.fullScreenSize = QtWidgets.QDesktopWidget().availableGeometry().size()
        if (userName == "chloé"):
            self.displayAnswer.selectAll()
            self.displayAnswer.setFontPointSize(14)
            self.displayQuestion.selectAll()
            self.displayQuestion.setFontPointSize(14)
            #self.sliderButtonLabel.setVisible(False)
            #self.sliderTextLabel.setVisible(False)
            #self.textPoliceSlider.setVisible(False)
            #self.buttonPoliceSlider.setVisible(False)

        self.dialog = Dialog
        self.__action = ""
        self.__data = data
        self.__databaseFile = databaseFile
        self.__course = course
        self.__chapter = chapter
        self.__userName = userName
        self.__currentChapter = ""
        self.__question = ""
        self.__answer = ""
        self.__index = 0
        self.__indexChapter = 0
        self.__formatQ = []
        self.__formatA = []
        if self.__chapter is not None : 
            self.__indexChapter = self.getIndexOfChapter()
        self.__numberOfQInChapter = 0
        self.validateChangeButton.setVisible(False)

        self.deleteButton.pressed.connect(lambda:self.buttonPressed(self.deleteButton))
        self.deleteButton.released.connect(lambda:self.buttonReleased(self.deleteButton))
        self.deleteButton.clicked.connect(self.delete)

        self.editButton.pressed.connect(lambda:self.buttonPressed(self.editButton))
        self.editButton.released.connect(lambda:self.buttonReleased(self.editButton))
        self.editButton.clicked.connect(self.edit)

        self.stopButton.pressed.connect(lambda:self.buttonPressed(self.stopButton))
        self.stopButton.released.connect(lambda:self.buttonReleased(self.stopButton))
        self.stopButton.clicked.connect(self.stop)

        self.nextButton.pressed.connect(lambda:self.buttonPressed(self.nextButton))
        self.nextButton.released.connect(lambda:self.buttonReleased(self.nextButton))
        self.nextButton.clicked.connect(self.next)

        self.previousButton.pressed.connect(lambda:self.buttonPressed(self.previousButton))
        self.previousButton.released.connect(lambda:self.buttonReleased(self.previousButton))
        self.previousButton.clicked.connect(self.previous)

        self.insertButton.pressed.connect(lambda:self.buttonPressed(self.insertButton))
        self.insertButton.released.connect(lambda:self.buttonReleased(self.insertButton))
        self.insertButton.clicked.connect(self.insert)
        #self.displayAnswer.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        #self.displayQuestion.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)

        self.displayChapter.setText(self.getchapterFromIndex())
        #self.textPoliceSlider.setValue(50)
        #self.textPoliceSlider.valueChanged.connect(self.changeTextPolice)
        #self.buttonPoliceSlider.setValue(50)
        #self.buttonPoliceSlider.valueChanged.connect(self.changeButtonPolice)

        self.readyToValidate = False
        self.validateChangeButton.clicked.connect(self.validateChange)
        self.displayChapter.repaint()
        self.validateChangeButton.repaint()
        self.display()
        
        self.formatMenuQ.setVisible(False)
        self.formatMenuQ.currentIndexChanged.connect(lambda:self.formatText(self.formatMenuQ, self.displayQuestion))
        self.formatMenuA.setVisible(False)
        self.formatMenuA.currentIndexChanged.connect(lambda:self.formatText(self.formatMenuA, self.displayAnswer))


    def getNumberOfQuestionsInChapter(self):
        count = 0
        for course in self.__data['courses']:
            if course['name'] == self.__course:
                if self.__chapter is not None:
                    for chapter in course['contentCourse']:
                        if chapter['name'] == self.__chapter:
                            count = len(chapter['contentChapter'])
                else : 
                    count = len(course['contentCourse'][self.__indexChapter]['contentChapter'])
        return count

    def getNumberOfChapters(self):
        for course in self.__data['courses']:
            if course['name'] == self.__course:
                return len(course['contentCourse'])

    def getIndexOfChapter(self):
        for course in self.__data['courses']:
            if course['name'] == self.__course:
                for chapter in course['contentCourse']:
                    if chapter['name'] == self.__chapter:
                        return course['contentCourse'].index(chapter)

    def getchapterFromIndex(self):
        for course in self.__data['courses']:
            if course['name'] == self.__course:
                return course['contentCourse'][self.__indexChapter]['name']

    def update(self):
        print("\n chapter name is : ", self.__chapter)
        self.__formatQ = []
        self.__formatA = []
        for course in self.__data['courses']:
            if course['name'] == self.__course:
                if self.__chapter is not None:
                    for chapter in course['contentCourse']:
                        if chapter['name'] == self.__chapter:
                            self.__question = chapter['contentChapter'][self.__index]['contentCard']['Q']
                            self.__answer = chapter['contentChapter'][self.__index]['contentCard']['A']
                            print("\n answer should be : ", chapter['contentChapter'][self.__index]['contentCard']['A'])
                            try :
                                self.__formatQ = chapter['contentChapter'][self.__index]['format']['Q']
                                self.__formatA = chapter['contentChapter'][self.__index]['format']['A']
                            except KeyError : 
                                print("No format for that card")
                else : 
                    try:
                        self.__question = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['Q']

                        self.__answer = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['A']
                        try :
                            self.__formatQ = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format']['Q']
                            self.__formatA = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format']['A']
                        except KeyError : 
                            print("No format for that card")
                    except IndexError:
                        print("no card here")
                    

    def getAction(self):
        return self.__action

    def edit(self):
        #self.dialog.resize(self.fullScreenSize)
        self.displayAnswer.setReadOnly(False)
        self.displayQuestion.setReadOnly(False)
        self.editButton.setVisible(False)
        self.nextButton.setVisible(False)
        self.previousButton.setVisible(False)
        self.stopButton.setVisible(False)
        self.insertButton.setVisible(False)
        self.deleteButton.setVisible(False)
        self.validateChangeButton.setVisible(True)
        self.editButton.setVisible(False)
        self.formatMenuQ.setVisible(True)
        self.formatMenuA.setVisible(True)

        while not self.readyToValidate :
            QtCore.QCoreApplication.processEvents()
        self.__question = self.displayQuestion.toPlainText()
        self.__answer = self.displayAnswer.toPlainText()

        specialFormatsQ, specialFormatsA, noFormatQ, noFormatA = self.addFormat()

        data = None
        with open(self.__databaseFile, 'r') as  jsonFile:
            db = json.load(jsonFile)

        for globalData in db['globalData']:
            if globalData['username'] == self.__userName:
                for course in globalData['data']['courses']: 
                    if course['name'] == self.__course:
                        course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['Q'] = self.__question
                        course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['A'] = self.__answer
                        if not (noFormatQ and noFormatA):
                            course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format'] = {'Q' : specialFormatsQ,
                             'A' : specialFormatsA}
                data = globalData['data']
        with open(self.__databaseFile, 'w') as reWriteFile:
            json.dump(db, reWriteFile)

        self.__data = data
        
        self.insertButton.setVisible(True)
        self.deleteButton.setVisible(True)
        self.editButton.setVisible(True)
        self.nextButton.setVisible(True)
        self.previousButton.setVisible(True)
        self.stopButton.setVisible(True)
        self.validateChangeButton.setVisible(False)
        self.readyToValidate = False
        self.deleteButton.setVisible(True)
        self.displayAnswer.setReadOnly(True)
        self.displayQuestion.setReadOnly(True)
        self.formatMenuQ.setVisible(False)
        self.formatMenuA.setVisible(False)
        self.display()
        
    def delete(self):
        data = None
        with open(self.__databaseFile, 'r') as  jsonFile:
            db = json.load(jsonFile)

        for globalData in db['globalData']:
            if globalData['username'] == self.__userName:
                for course in globalData['data']['courses']: 
                    if course['name'] == self.__course:
                        course['contentCourse'][self.__indexChapter]['contentChapter'].pop(self.__index)
                data = globalData['data']
        with open(self.__databaseFile, 'w') as reWriteFile:
            json.dump(db, reWriteFile)

        self.__data = data

        if self.__index == 0 and (self.__chapter is None or self.__indexChapter == 0):
            self.next()
        elif self.__index is not 0 or self.__indexChapter > 0 : 
            self.previous()
        self.displayAnswer.setReadOnly(True)
        self.displayQuestion.setReadOnly(True)

    def stop(self):
        self.__action = "stop"
        self.dialog.done(0)

    def next(self):
        nOfQ = self.getNumberOfQuestionsInChapter()
        #print(nOfQ)

        if self.__index < nOfQ - 1:
            self.__index += 1
            #print(self.__index)
            self.display()
        #go to next chapter 
        elif (self.__index == nOfQ - 1) and (self.__chapter == None) and (self.__indexChapter < self.getNumberOfChapters() - 1):
            self.__index = 0
            self.__indexChapter += 1
            while self.getNumberOfQuestionsInChapter() == 0 and self.__indexChapter < self.getNumberOfChapters() - 1:
                self.__indexChapter += 1
            self.display()
        else :
            self.__index = nOfQ 
            self.displayQuestion.setPlainText("")
            self.displayAnswer.setPlainText("")
            self.displayCounter.setText("0/0")

    def previous(self):
        if self.__index > 0 :
            self.__index -= 1
            self.display()
            #self.getFormat()
        #go to previous chapter
        elif (self.__index == 0)and(self.__chapter == None) and (self.__indexChapter > 0):
            self.__indexChapter -= 1
            while self.getNumberOfQuestionsInChapter() == 0 and self.__indexChapter > 0:
                self.__indexChapter -= 1
            self.__index = self.getNumberOfQuestionsInChapter() - 1
            self.display()
            #self.getFormat()
        else :
            self.__index = -1
            self.displayQuestion.setPlainText("")
            self.displayAnswer.setPlainText("")
            self.displayCounter.setText("0/0")

    def display(self):
        self.update()
        self.displayQuestion.setPlainText(self.__question)
        self.displayAnswer.setPlainText(self.__answer)
        self.displayCounter.setText(str(self.__index + 1) + "/" + str (self.getNumberOfQuestionsInChapter()))
        self.displayChapter.setText(self.getchapterFromIndex())
        self.displayAnswer.repaint()
        self.displayQuestion.repaint()
        self.displayCounter.repaint()
        self.getFormat()

    def buttonPressed(self, widget):
        widget.resize(0.95 * widget.width(), 0.95 * widget.height())
    
    def buttonReleased(self, widget):
        widget.resize((1/0.95) * widget.width(), (1/0.95) * widget.height())
  
    def validateChange(self):
        self.readyToValidate = True
    
    def insert(self):
        self.displayAnswer.setReadOnly(False)
        self.displayQuestion.setReadOnly(False)
        self.editButton.setVisible(False)
        self.nextButton.setVisible(False)
        self.previousButton.setVisible(False)
        self.stopButton.setVisible(False)
        self.deleteButton.setVisible(False)
        self.validateChangeButton.setVisible(True)
        self.editButton.setVisible(False)
        self.displayQuestion.setText("")
        self.displayAnswer.setText("")
        self.insertButton.setVisible(False)
        self.formatMenuQ.setVisible(True)
        self.formatMenuA.setVisible(True)

        self.__index += 1
        self.displayCounter.setText(str(self.__index + 1) + "/" + str (self.getNumberOfQuestionsInChapter()+1) )
        while not self.readyToValidate :
            QtCore.QCoreApplication.processEvents()
        
        self.__question = self.displayQuestion.toPlainText()
        self.__answer = self.displayAnswer.toPlainText()
        specialFormatsQ, specialFormatsA, noFormatQ, noFormatA = self.addFormat()

        data = None
        with open(self.__databaseFile, 'r') as  jsonFile:
            db = json.load(jsonFile)

        for globalData in db['globalData']:
            if globalData['username'] == self.__userName:
                for course in globalData['data']['courses']: 
                    if course['name'] == self.__course:
                        course['contentCourse'][self.__indexChapter]['contentChapter'].insert(self.__index, {'contentCard':{'Q' : self.__question,
                        'A' :self.__answer}})
                        if not (noFormatQ and noFormatA) :
                            course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format'] = {
                                'Q' : specialFormatsQ,
                                'A' : specialFormatsA}
                data = globalData['data']
        with open(self.__databaseFile, 'w') as reWriteFile:
            json.dump(db, reWriteFile)

        self.insertButton.setVisible(True)
        self.__data = data
        self.editButton.setVisible(True)
        self.nextButton.setVisible(True)
        self.previousButton.setVisible(True)
        self.stopButton.setVisible(True)
        self.deleteButton.setVisible(True)
        self.insertButton.setVisible(True)
        self.validateChangeButton.setVisible(False)
        self.readyToValidate = False
        self.deleteButton.setVisible(True)
        self.displayAnswer.setReadOnly(True)
        self.displayQuestion.setReadOnly(True)
        self.formatMenuQ.setVisible(False)
        self.formatMenuA.setVisible(False)
        self.display()

    def getFormat(self):
        self.displayQuestion.setReadOnly(False)
        cursorQ = self.displayQuestion.textCursor()
        cursorQ.movePosition(QtGui.QTextCursor.Start)
        i = 0
        while i < len(self.__formatQ):
            cursorQ.movePosition(QtGui.QTextCursor.NextCharacter, mode=QtGui.QTextCursor.KeepAnchor) 
            totalCharacterFormat = QtGui.QTextCharFormat()
            font = self.displayQuestion.currentFont()
            fmtCaracter = self.__formatQ[i]
            for fmt in fmtCaracter :
                if fmt is 'b':
                    font.setBold(True)
                    print ('b')
                elif fmt is 'u':
                    font.setUnderline(True)
                    print('u')
                elif fmt is 'i':
                    font.setItalic(True)
                    print('i')
                elif fmt is 's':
                    font.setStrikeOut(True)
            totalCharacterFormat.setFont(font)
            cursorQ.setCharFormat(totalCharacterFormat)
            cursorQ.movePosition(QtGui.QTextCursor.NextCharacter) #reset anchor to get a single character at each iteration
            i += 1
        self.displayAnswer.setReadOnly(False)
        cursorA = self.displayAnswer.textCursor()
        cursorA.movePosition(QtGui.QTextCursor.Start)
        i = 0
        while i < len(self.__formatA):
            cursorA.movePosition(QtGui.QTextCursor.NextCharacter, mode=QtGui.QTextCursor.KeepAnchor)
            totalCharacterFormat = QtGui.QTextCharFormat()
            font = self.displayAnswer.currentFont()
            fmtCaracter = self.__formatA[i]
            for fmt in fmtCaracter :
                if fmt is 'b':
                    font.setBold(True)
                elif fmt is 'u':
                    font.setUnderline(True)
                elif fmt is 'i':
                    font.setItalic(True)
                elif fmt is 's':
                    font.setStrikeOut(True)
            totalCharacterFormat.setFont(font)
            cursorA.setCharFormat(totalCharacterFormat)
            cursorA.movePosition(QtGui.QTextCursor.NextCharacter)
            i += 1
        self.displayQuestion.setReadOnly(True)
        self.displayAnswer.setReadOnly(True)

    def formatText(self, menu, textWidget):
        index = menu.currentIndex()
        fmt = QtGui.QTextCharFormat()
        cursor = textWidget.textCursor()#QtGui.QTextCursor()
        #self.questionInput.setTextCursor(cursor)
        font = textWidget.currentFont()
        color = QtGui.QColor()
        
        if index is 1 :
            font.setBold(True)
        elif index is 2:
            font.setUnderline(True)
        elif index is 3:
            font.setItalic(True)
        elif index is 4:
            font.setStrikeOut(True)
        elif index is 5 : 
            color.setAlpha(0)
            color.setRed(255)
            color.setGreen(0)
            color.setBlue(0)
            textWidget.setTextColor(color)
        elif index is 6 : 
            color.setAlpha(0)
            color.setRed(0)
            color.setGreen(255)
            color.setBlue(0)
            textWidget.setTextColor(color)
        elif index is 0 :
            color.setNamedColor("black")
            font.setBold(False)
            font.setUnderline(False)
            font.setItalic(False)
            font.setStrikeOut(False)
            textWidget.setTextColor(color)

        fmt.setFont(font)
        cursor.setCharFormat(fmt)
        cursor.setCharFormat(fmt)
    
    def addFormat(self):
        i = 0
        fmt = QtGui.QTextCharFormat()
        cursorQ = self.displayQuestion.textCursor()
        cursorQ.movePosition(QtGui.QTextCursor.Start)
        specialFormatsQ = []
        while i < len(self.__question): 
            specialFormatsQ.append([])
            cursorQ.movePosition(QtGui.QTextCursor.NextCharacter)
            fmt = cursorQ.charFormat()
            print (fmt.fontWeight())
            if fmt.fontUnderline():
                specialFormatsQ[i].append('u')
            if fmt.fontItalic():
                specialFormatsQ[i].append('i')
            if fmt.fontStrikeOut():
                specialFormatsQ[i].append('s')
            if fmt.fontWeight() > 50:  #normal weight is 50, greater means bolded text
                specialFormatsQ[i].append('b')
            i += 1 

        i = 0
        cursorA = self.displayAnswer.textCursor()
        cursorA.movePosition(QtGui.QTextCursor.Start)
        specialFormatsA = []
        while i < len(self.__answer): 
            specialFormatsA.append([])
            cursorA.movePosition(QtGui.QTextCursor.NextCharacter)
            fmt = cursorA.charFormat()
            print (fmt.fontWeight())
            if fmt.fontUnderline():
                specialFormatsA[i].append('u')
            if fmt.fontItalic():
                specialFormatsA[i].append('i')
            if fmt.fontStrikeOut():
                specialFormatsA[i].append('s')
            if fmt.fontWeight() > 50:  #normal weight is 50, greater means bolded text
                specialFormatsA[i].append('b')
            i += 1 
        data = None
        noFormatQ = False
        for l in specialFormatsQ : 
            if len(l) is not 0 : 
                noFormatQ = False
                break
            else :
                noFormatQ = True

        noFormatA = False
        for l in specialFormatsA : 
            if len(l) is not 0 : 
                noFormatA = False
                break
            else :
                noFormatA = True
        
        return specialFormatsQ, specialFormatsA, noFormatQ, noFormatA