class Card:
    
    def __init__(self, id, Q, A, course = None, chapter = None):
        self.__question =  Q
        self.__answer = A
        self.__course = course
        self.__QType, self.__AType = self.setQandAType()
        self.__previousResults = []
        self.__id = id
        self.__chapter = chapter
        self.__questionCounter = 1
        self.__answerCounter = 1

    @property
    def getQuestion(self):
        return self.__question

    @property
    def getAnswer(self):
        return self.__answer

    @property
    def getQType(self): 
        return self.__QType

    @property
    def getAType(self):
        return self.__AType
    
    @property
    def getPreviousResults(self):
        return self.__previousResults
    
    def addResult(self, result):
        self.__previousResults.append(result)

    def changeQuestion(self, newQuestion) : 
        self.__question = newQuestion

    def setQandAType(self):
        return ("", "")
    
    def changeCourse(self, newCourse):
        self.__course = newCourse

    def changeChapter(self, newChapter):
        self.__chapter = newChapter

    def addQuestion(self, question):
        self.__question += "\n " + question
        self.__questionCounter += 1

    def addAnswer(self, answer):
        if (self.__answerCounter == self.__questionCounter - 1):
            self.__answer += "\n " + answer
            self.__answerCounter += 1
        else : 
            raise AttributeError

