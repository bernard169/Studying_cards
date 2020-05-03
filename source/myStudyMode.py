from PyQt5 import QtCore, QtGui, QtWidgets
from studyMode import Ui_studyModeDialog as studyDialog 
from PyQt5.QtWidgets import QMessageBox
import random
import json
import time
import utils

class myStudyDialog(studyDialog):
    def setupUi(self, dialog, username, data, database, databaseFile, itemsToStudy, isRandom, spacingMistakes, minPointsRequired):
        super().setupUi(dialog)
        self.__userName = username
        self.__isRandom = isRandom
        self.__dialog = dialog
        self.__data = data
        self.__database = database
        self.__databaseFile = databaseFile
        self.__itemsToStudy = []
        for s in itemsToStudy : #splitting string to get parent and child in a list
            i = s.split("{")
            if len(i) > 1:
                self.__itemsToStudy.append(i)
            else:
                self.__itemsToStudy.append(i[0])
        self.__indexChapter = 0
        self.__index = -1
        self.__nOfQuestions = 0
        self.__course = self.__itemsToStudy[0] if type(self.__itemsToStudy[0]) is str else self.__itemsToStudy[0][0]
        self.__chapter = None if type(self.__itemsToStudy[0]) is str else self.__itemsToStudy[0][1]
        self.__nOfCoursesToStudy = len([item for item in self.__itemsToStudy if (type(item) is str)])
        lCoursesToStudy = []
        for item in self.__itemsToStudy :
            if type(item) is not str :
                if item[0] not in lCoursesToStudy :
                    lCoursesToStudy.append(item[0])
                    self.__nOfCoursesToStudy += 1
        self.__nOfChaptersToStudy = len([item for item in self.__itemsToStudy if type(item) is not str]) #only chapters have a len 2 entry in this list
        self.__question = ""
        self.__answer = ""
        self.__formatA = []
        self.__formatQ = []
        self.__coursesDone = 0
        self.__chaptersDone = 0
        self.__neededWork = []
        self.__playbackCounter = 0
        self.__spacingMistakes = spacingMistakes if spacingMistakes > 2 else 3
        self.__unAnsweredQuestions = []
        self.getAllQuestionsByIndex()
        self.__pointsRequired = 1
        if minPointsRequired > 1 :
            self.__pointsRequired = minPointsRequired
        #self.__pointsRequired = 2 if isRandom else 1
        self.__prevQIsWrong = False
        self.__qActive = True
        self.validateQButton.setVisible(False)
        self.needWorkButton.setVisible(False)
        self.cancelChangeButton.setVisible(False)
        self.validateChangeButton.setVisible(False)
        self.formatMenu.setVisible(False)
        self.nextQuestion()
        self.viewAnswerButton.clicked.connect(self.viewAnswer)
        self.stopButton.clicked.connect(self.stop)
        self.needWorkButton.clicked.connect(self.needsWork)
        self.validateQButton.clicked.connect(self.validateQuestion)
        self.validateChangeButton.clicked.connect(self.validateChange)
        self.cancelChangeButton.clicked.connect(self.cancelChange)
        self.editButton.clicked.connect(self.edit)
        self.formatMenu.currentIndexChanged.connect(lambda:utils.formatText(self.formatMenu, self.displayQA))
        for button in self.__dialog.findChildren(QtWidgets.QPushButton):
            button.pressed.connect(lambda:utils.buttonPressed(button))
            button.released.connect(lambda:utils.buttonReleased(button))

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

    def getchapterFromIndex(self, index=None):
        if index is None:
            index = self.__indexChapter
        for course in self.__data['courses']:
            if course['name'] == self.__course:
                return course['contentCourse'][index]['name']

    def getAllQuestionsByIndex(self):
        #[[cours1, chapitre1], [cours1, chapitre2]]
        for elem in self.__itemsToStudy :
            if type(elem) is str :
                #whole course
                for course in self.__data['courses']:
                    if course['name'] == elem :
                        courseIndex = self.__data['courses'].index(course)
                        for chapter in course['contentCourse']:
                            chapterIndex = course['contentCourse'].index(chapter)
                            for card in chapter['contentChapter']:
                                cardIndex = chapter['contentChapter'].index(card)
                                self.__unAnsweredQuestions.append([courseIndex, chapterIndex, cardIndex, 0])
            else :
                for course in self.__data['courses']:
                    if course['name'] == elem[0]:
                        print("elem 0 found")
                        courseIndex = self.__data['courses'].index(course)
                        for chapter in course['contentCourse']:
                            if chapter['name'] == elem[1]:
                                print("elem 1 found")
                                chapterIndex = course['contentCourse'].index(chapter)
                                for card in chapter['contentChapter']:
                                    cardIndex = chapter['contentChapter'].index(card)
                                    self.__unAnsweredQuestions.append([courseIndex, chapterIndex, cardIndex, 0])

    def nextQuestion(self):
        nOfQ = self.getNumberOfQuestionsInChapter()
        if len(self.__neededWork) > 0:
            self.__playbackCounter += 1
        if self.__prevQIsWrong : 
            self.viewQuestion()
        elif self.__playbackCounter > self.__spacingMistakes:
            print(self.__neededWork)
            self.__chapter = self.__neededWork[0][0]
            self.__index = self.__neededWork[0][1]
            self.__indexChapter = self.getIndexOfChapter()
            self.__neededWork.pop(0)
            if len(self.__neededWork) > 0:
                self.__playbackCounter -= (self.__spacingMistakes - 1)
            else :
                self.__playbackCounter = 0
            self.viewQuestion()
        elif self.__isRandom :
            for card in self.__unAnsweredQuestions :
                if card[3] >= self.__pointsRequired :
                    print("card known")
                    self.__unAnsweredQuestions.remove(card)
                    for infos in self.__neededWork : 
                        if infos[0] == self.getchapterFromIndex(card[1]) and infos[1] == card[2]:
                            self.__neededWork.remove(infos)
            if len(self.__unAnsweredQuestions) == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Terminer")
                msg.setText("Félicitations ! Tu as terminé {}".format("ces chapitres." if self.__chapter is not None else "ce cours."))
                msg.setIcon(QMessageBox.Information)
                ex = msg.exec_()
                self.__dialog.done(0)
            else:
                nextElem = self.__itemsToStudy[random.randrange(0, len(self.__itemsToStudy), 1)]
                print("next elem is : \n")
                print(nextElem)
                if type(nextElem) is str:
                    self.__course = nextElem
                    self.__chapter = None 
                else : 
                    self.__course = nextElem[0]
                    self.__chapter = nextElem[1]
                
                self.__nOfQuestions = self.getNumberOfQuestionsInChapter()
                random.seed(int(time.time()))# % self.__nOfQuestions)
                card = self.__unAnsweredQuestions[random.randrange(0, len(self.__unAnsweredQuestions), 1)]
                self.__indexChapter = card[1]
                self.__index = card[2]
                #self.__index = random.randrange(0, self.__nOfQuestions, 1)
                print(self.__index)
                self.viewQuestion()
        else:
            if self.__index < nOfQ - 1:
                self.__index += 1
                #print(self.__index)
                self.viewQuestion()
            #go to next chapter 
            elif (self.__index == nOfQ - 1) and (len(self.__neededWork) > 0) : 
                self.__chapter = self.__neededWork[0][0]
                self.__index = self.__neededWork[0][1]
                self.__indexChapter = self.getIndexOfChapter() if self.__chapter is not None else self.__indexChapter 
                self.__neededWork.pop(0)
                if len(self.__neededWork) > 0:
                    self.__playbackCounter -= 2
                else :
                    self.__playbackCounter = 0
                self.viewQuestion()
            elif (self.__index == nOfQ - 1) and (self.__chapter == None) and (self.__indexChapter < self.getNumberOfChapters() - 1):
                #end of chapter, whole course selected, not the last chapter
                self.__index = 0
                self.__indexChapter += 1
                while self.getNumberOfQuestionsInChapter() == 0 and self.__indexChapter < self.getNumberOfChapters() - 1:
                    self.__indexChapter += 1
                self.viewQuestion()
            elif (self.__index == nOfQ - 1) and (self.__chapter == None) and (self.__indexChapter == self.getNumberOfChapters()-1) and (self.__coursesDone < self.__nOfCoursesToStudy - 1):
                self.__coursesDone += 1
                self.__chaptersDone += 1
                if type(self.__itemsToStudy[self.__chaptersDone]) is str :
                    self.__course = self.__itemsToStudy[self.__chaptersDone]
                    self.__indexChapter = 0
                    self.__index = 0
                    self.__chapter = None
                else :
                    self.__course = self.__itemsToStudy[self.__chaptersDone][0]
                    self.__chapter = self.__itemsToStudy[self.__chaptersDone][1]
                    self.__index = 0
                    self.__indexChapter = self.getIndexOfChapter()
                    print("index chapter here : ")
                    print(self.__indexChapter)
                self.viewQuestion()
            elif (self.__index == nOfQ - 1) and (self.__chapter is not None) and (self.__chaptersDone < self.__nOfChaptersToStudy - 1):
                self.__chaptersDone += 1
                self.__course = self.__itemsToStudy[self.__chaptersDone][0]
                self.__chapter = self.__itemsToStudy[self.__chaptersDone][1]
                self.__index = 0
                self.__indexChapter = self.getIndexOfChapter()
                self.viewQuestion()
            elif (self.__index == nOfQ - 1) and (self.__chaptersDone == self.__nOfChaptersToStudy -1): 
                msg = QMessageBox()
                msg.setWindowTitle("Terminer")
                msg.setText("Félicitations ! Tu as terminé {}".format("ces chapitres." if self.__chapter is not None else "ce cours."))
                msg.setIcon(QMessageBox.Information)
                ex = msg.exec_()
            else :
                self.__index = nOfQ 
                self.displayQA.setPlainText("")
                self.counterLabel.setText("0/0")
        

    def getQA(self):
        self.__formatQ = []
        self.__formatA = []
        for course in self.__data['courses']:
            if course['name'] == self.__course:
                courseIndex = self.__data['courses'].index(course)
                if self.__chapter is not None:
                    for chapter in course['contentCourse']:
                        if chapter['name'] == self.__chapter:
                            chapterIndex = course['contentCourse'].index(chapter)
                            for cardInfo in self.__unAnsweredQuestions :
                                if cardInfo[:3] == [courseIndex, chapterIndex, self.__index]:
                                    if cardInfo[3] < self.__pointsRequired:
                                        self.__question = chapter['contentChapter'][self.__index]['contentCard']['Q']
                                        self.__answer = chapter['contentChapter'][self.__index]['contentCard']['A']
                                        try :
                                            self.__formatQ = chapter['contentChapter'][self.__index]['format']['Q']
                                            self.__formatA = chapter['contentChapter'][self.__index]['format']['A']
                                        except KeyError : 
                                            print("No format for that card")
                                    else : 
                                        #self.__unAnsweredQuestions.remove(cardInfo)
                                        self.nextQuestion()
                else : 
                    try:
                        for cardInfo in self.__unAnsweredQuestions :
                                if cardInfo[:3] == [courseIndex, self.__indexChapter, self.__index]:
                                    if cardInfo[3] < self.__pointsRequired:
                                        self.__question = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['Q']

                                        self.__answer = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['A']
                                        try :
                                            self.__formatQ = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format']['Q']
                                            self.__formatA = course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format']['A']
                                        except KeyError : 
                                            print("No format for that card")
                                    else :
                                        #self.__unAnsweredQuestions.remove(cardInfo)
                                        self.nextQuestion()
                    except IndexError:
                        print("no card here")

    def viewQuestion(self):
        self.getQA()
        self.__qActive = True
        self.displayQA.setPlainText(self.__question)
        print("Question is : ")
        print(self.__question)
        #self.displayAnswer.setPlainText(self.__answer)
        self.counterLabel.setText(str(self.__index + 1) + "/" + str (self.getNumberOfQuestionsInChapter()))
        #self.displayChapter.setText(self.getchapterFromIndex())
        self.chapterLabel.setText(self.__chapter if self.__chapter is not None else self.getchapterFromIndex())
        self.displayQA.repaint()
        self.counterLabel.repaint()
        utils.getFormat(self.displayQA, self.__formatQ)

    def viewAnswer(self):
        self.viewAnswerButton.setVisible(False)
        self.validateQButton.setVisible(True)
        self.needWorkButton.setVisible(True)
        self.getQA()
        self.__qActive = False
        self.displayQA.setPlainText(self.__answer)
        self.counterLabel.setText(str(self.__index + 1) + "/" + str (self.getNumberOfQuestionsInChapter()))
        self.displayQA.repaint()
        self.counterLabel.repaint()
        utils.getFormat(self.displayQA, self.__formatA)

    def validateQuestion(self):
        #add one point to this question
        courseIndex = -1
        chapterIndex = -1
        cardIndex = -1
        cardFound = False
        self.__chapter = self.getchapterFromIndex() if self.__chapter is None else self.__chapter
        for course in self.__data['courses']:
            if course['name'] == self.__course : 
                courseIndex = self.__data['courses'].index(course)
                for chapter in course['contentCourse']:
                    if chapter['name'] == self.__chapter:
                        chapterIndex = course['contentCourse'].index(chapter)
                        for card in chapter['contentChapter']:
                            if (card['contentCard']['Q'] == self.__question) and (card['contentCard']['A'] == self.__answer) :
                                cardIndex = chapter['contentChapter'].index(card)
        if not self.__prevQIsWrong :
            for cardInfo in self.__unAnsweredQuestions :
                if cardInfo[:3] == [courseIndex, chapterIndex, cardIndex]:
                    cardInfo[3] += 1
                    cardFound = True
                    print("Good for you :) \n")
            if not cardFound :
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("Error : cannot find the specified card. Please contact a contributor.")
                msg.setIcon(QMessageBox.Critical)
                ex = msg.exec_()
                self.__dialog.done(0)
        self.__prevQIsWrong = False
        self.viewAnswerButton.setVisible(True)
        self.validateQButton.setVisible(False)
        self.needWorkButton.setVisible(False)
        self.nextQuestion()
    
    def needsWork(self):
        #add a function to come back to this question 
        self.__chapter = self.getchapterFromIndex() if self.__chapter is None else self.__chapter
        if not self.__prevQIsWrong :
            self.__neededWork.append((self.__chapter, self.__index))
        self.viewAnswerButton.setVisible(True)
        self.validateQButton.setVisible(False)
        self.needWorkButton.setVisible(False)
        self.__prevQIsWrong = True
        self.nextQuestion()

    def getAction(self): 
        pass

    def stop(self):
        self.__dialog.done(0)

    def edit(self):
        self.validateChangeButton.setVisible(True)
        self.cancelChangeButton.setVisible(True)
        self.formatMenu.setVisible(True)
        self.editButton.setVisible(False)
        self.validateQButton.setVisible(False)
        self.needWorkButton.setVisible(False)
        self.viewAnswerButton.setVisible(False)

        self.displayQA.setReadOnly(False)

    def validateChange(self):
        self.validateChangeButton.setVisible(False)
        self.cancelChangeButton.setVisible(False)
        self.formatMenu.setVisible(False)
        self.editButton.setVisible(True)
        text = self.displayQA.toPlainText()
        formats, noFormat = utils.addFormat(self.displayQA, text)
        if self.__qActive :
            self.__question = text
            self.viewAnswerButton.setVisible(True)
        else :
            self.__answer = text
            self.validateQButton.setVisible(True)
            self.needWorkButton.setVisible(True)

        data = None
        with open(self.__databaseFile, 'r') as  jsonFile:
            db = json.load(jsonFile)

        for globalData in db['globalData']:
            if globalData['username'] == self.__userName:
                for course in globalData['data']['courses']: 
                    if course['name'] == self.__course:
                        course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['Q'] = self.__question
                        course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['contentCard']['A'] = self.__answer
                        if not(noFormat) and self.__qActive:
                            course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format']['Q'] = formats
                        elif not(noFormat) and not(self.__qActive):
                            course['contentCourse'][self.__indexChapter]['contentChapter'][self.__index]['format']['A'] = formats
                data = globalData['data']
        with open(self.__databaseFile, 'w') as reWriteFile:
            json.dump(db, reWriteFile)
        self.__data = data
        
        ####################
        ### INSERT HERE ####
        ####################
        self.displayQA.setReadOnly(True)

    def cancelChange(self):
        self.validateChangeButton.setVisible(False)
        self.cancelChangeButton.setVisible(False)
        self.formatMenu.setVisible(False)
        self.editButton.setVisible(True)
        if self.__qActive :
            self.viewAnswerButton.setVisible(True)
            self.viewQuestion()
        else :
            self.validateQButton.setVisible(True)
            self.needWorkButton.setVisible(True)
            self.viewAnswer()

        self.displayQA.setReadOnly(True)