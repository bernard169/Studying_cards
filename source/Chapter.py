
class Chapter:

    def __init__(self,  name, course):
        self.__name = name
        self.__course = course
        self.__content = []
    
    @property
    def getName(self):
        return self.__name

    @property
    def getCourse(self):
        return self.__course

    @property
    def getContent(self):
        return self.__content

    def changeName(self, newName):
        self.__name = newName

    def addCard(self, card):
        self.__content.append(card)

    def countCards(self):
        return len(self.__content)

