import Card
import Chapter

class Course:

    def __init__(self, name):
        self.__name = name
        self.__content = []
        self.__individualCardsCount = 0

    def addChapter(self, chapter):
        self.__content.append(chapter)
    
    '''
    Used only to bypass default structure and add the card directly in
     the course (no chapter associated)
    '''
    def addCard(self, card):
        self.__content.append(card)
        self.__individualCardsCount += 1

    def getChapters(self):
        chapters = []
        for elem in self.__content : 
            if type(elem) == Chapter : 
                chapters.append(elem.getName())
        return chapters

    def countCards(self):
        counter = 0
        for elem in self.__content : 
            if type(elem) == Chapter : 
                counter += elem.countCards()
            elif type(elem) == Card : 
                counter += 1
            else : 
                raise AttributeError
        return counter