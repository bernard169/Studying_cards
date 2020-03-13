from PyQt5 import QtCore, QtGui, QtWidgets
import explorerMain

class MyExplorerMain(explorerMain.Ui_MainWindow):
    def setupUi(self, Dialog, dataTree):
        self.__action = ""
        self.dialog = Dialog
        super().setupUi(Dialog)
        self.coursesView.setHeaderLabels(["Cours", "Nombre de cartes"])
        self.buildTree(dataTree)
        self.studyButton.clicked.connect(self.study)
        self.loginButton.clicked.connect(self.logout)
        self.createButton.clicked.connect(self.create)

    def addItem (self, name, numberOfCards, parent=0):
        if not parent:
            parent = self.coursesView
        return QtWidgets.QTreeWidgetItem(parent, [name, str(numberOfCards)])

    def buildTree(self, dataTree):
        for course in dataTree["courses"]:
            cardsInCourse = 0
            for chapter in course["contentCourse"]:
                for card in chapter["contentChapter"]:
                    cardsInCourse += 1
            courseItem = self.addItem(course["name"], cardsInCourse)
            for chapter in course["contentCourse"]:
                cardsInChapter = 0
                for card in chapter["contentChapter"]:
                    cardsInChapter += 1
                self.addItem(chapter["name"], cardsInChapter, courseItem)      
    
    def study(self):
        self.__action = "study"
        self.dialog.done(0)

    def create(self):
        self.__action = "create"
        self.dialog.done(0)

    def logout(self):
        self.__action = "logout"
        self.dialog.done(0)
    
    def getAction(self):
        return self.__action

