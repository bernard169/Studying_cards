from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
import createMenu
from myAddStructuralItemDialog import MyAddStructuralItemDialog

class MyCreatePageDialog(createMenu.Ui_createPageDialog):
    def setupUi(self, createPageDialog, dataTree, databaseFile, userName):
        super().setupUi(createPageDialog)
        self.__relPathToDatabase = databaseFile
        self.__userName = userName
        self.__action = ""
        self.__data = dataTree
        self.dialog = createPageDialog
        self.coursesView.setHeaderLabels(["Cours", "Nombre de cartes"])
        self.buildTree()
        self.homeButton.pressed.connect(lambda:self.buttonPressed(self.homeButton))
        self.homeButton.released.connect(lambda:self.buttonReleased(self.homeButton))
        self.homeButton.clicked.connect(self.home)

        self.addCourseButton.pressed.connect(lambda:self.buttonPressed(self.addCourseButton))
        self.addCourseButton.released.connect(lambda:self.buttonReleased(self.addCourseButton))
        self.addCourseButton.clicked.connect(self.addCourse)

        self.addChapterButton.pressed.connect(lambda:self.buttonPressed(self.addChapterButton))
        self.addChapterButton.released.connect(lambda:self.buttonReleased(self.addChapterButton))
        self.addChapterButton.clicked.connect(self.addChapter)

        self.addCardButton.pressed.connect(lambda:self.buttonPressed(self.addCardButton))
        self.addCardButton.released.connect(lambda:self.buttonReleased(self.addCardButton))
        self.addCardButton.clicked.connect(self.addCard)

        self.removeCourseButton.pressed.connect(lambda:self.buttonPressed(self.removeCourseButton))
        self.removeCourseButton.released.connect(lambda:self.buttonReleased(self.removeCourseButton))
        self.removeCourseButton.clicked.connect                                                 (self.removeCourse)

        self.removeChapterButton.pressed.connect(lambda:self.buttonPressed(self.removeChapterButton))
        self.removeChapterButton.released.connect(lambda:self.buttonReleased(self.removeChapterButton))
        self.removeChapterButton.clicked.connect                                                (self.removeChapter)

        self.editButton.pressed.connect(lambda:self.buttonPressed(self.editButton))
        self.editButton.released.connect(lambda:self.buttonReleased(self.editButton))
        self.editButton.clicked.connect(self.edit)

        self.previewButton.pressed.connect(lambda:self.buttonPressed(self.previewButton))
        self.previewButton.released.connect(lambda:self.buttonReleased(self.previewButton))
        self.previewButton.clicked.connect(self.preview)

        self.coursesView.header().resizeSection(0, self.coursesView.width() * (2/3))

    def addItem (self, name, numberOfCards, parent=0):
        if not parent:
            parent = self.coursesView
        return QtWidgets.QTreeWidgetItem(parent, [name, str(numberOfCards)])

    def buildTree(self):
        self.coursesView.clear()
        dataTree = self.__data
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
    
    def addCourse(self):
        data = None
        #ask user for course's name
        #app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = MyAddStructuralItemDialog()
        ui.setupUi(Dialog)
        ui.setContent("cours")
        Dialog.exec()

        action, name = ui.getInfos()

        if action == "cancel":
            return None
        with open(self.__relPathToDatabase, 'r') as  jsonFile:
            database = json.load(jsonFile)

        for globalData in database['globalData']:
            if globalData['username'] == self.__userName:
                globalData['data']['courses'].append(
                    {'name' : name,
                     'contentCourse' : []})
                data = globalData['data']
        
        with open(self.__relPathToDatabase, 'w') as reWriteFile:
            json.dump(database, reWriteFile)

        self.__data = data
        self.buildTree()
        return action

    def addChapter(self):
        data = None
        parentCourse = ""
        selected = self.coursesView.selectedItems()
        if len(selected) == 0 :
            return None
        for item in selected : 
            parentCourse = item.text(0)

        #ask user for course's name
        Dialog = QtWidgets.QDialog()
        ui = MyAddStructuralItemDialog()
        ui.setupUi(Dialog)
        ui.setContent("chapitre")
        Dialog.exec()
        
        action, name = ui.getInfos()

        if action == "cancel":
            return None
        with open(self.__relPathToDatabase, 'r') as  jsonFile:
            database = json.load(jsonFile)
        
        for globalData in database['globalData']:
            if globalData['username'] == self.__userName:
                for course in globalData['data']['courses']: 
                    if course['name'] == parentCourse :
                        course['contentCourse'].append(
                            {"name" : name,
                             "contentChapter" : []}
                        )
                data = globalData['data']
        
        with open(self.__relPathToDatabase, 'w') as reWriteFile:
            json.dump(database, reWriteFile)

        self.__data = data
        self.buildTree()
        return action

    def addCard(self):
        selected = self.coursesView.selectedItems()
        itemSelectedType = ""
        for item in selected : 
            itemSelected = item.text(0)
            if self.coursesView.indexOfTopLevelItem(item) < 0 :
                itemSelectedType = "chapter"
            else : 
                itemSelectedType = "course"
        if itemSelectedType != "chapter" : 
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Vous devez créer une fiche dans un" +              " chapitre")
            msg.setIcon(QMessageBox.Warning)
            ex = msg.exec_()
            return None
        else : 
            self.__action = "addCard" + "_:_" + selected[0].parent().text(0) + "_:_" + selected[0].text(0)
            self.dialog.done(0)
    
    def removeCourse(self):
        selected = self.coursesView.selectedItems()
        data = None
        if len(selected) == 0:
            return None
        with open(self.__relPathToDatabase, 'r') as  jsonFile:
            database = json.load(jsonFile)
        removedCourse = {}
        for item in selected : 
            for globalData in database['globalData']:
                if globalData['username'] == self.__userName:
                    data = globalData['data']
                    for course in globalData['data']['courses'] :
                        if course['name'] == item.text(0) :
                            removedCourse = course
                    try : 
                        globalData['data']['courses'] .remove(removedCourse)
                    except ValueError :
                        msg = QMessageBox()
                        msg.setWindowTitle("Warning")
                        msg.setText("Vous n'avez pas" +                     " sélectionné un cours")
                        msg.setIcon(QMessageBox.Warning)
                        ex = msg.exec_()

        with open(self.__relPathToDatabase, 'w') as reWriteFile:
            json.dump(database, reWriteFile)

        self.__data = data
        self.buildTree()

    def removeChapter(self):
        selected = self.coursesView.selectedItems()
        if len(selected) == 0:
            return None
        data = None
        with open(self.__relPathToDatabase, 'r') as  jsonFile:
            database = json.load(jsonFile)
        for item in selected : 
            for globalData in database['globalData'] :
                if globalData['username'] == self.__userName :
                    data = globalData['data']
                    for course in data['courses'] :
                        for chapter in course['contentCourse'] :
                            if chapter['name'] == item.text(0) :
                                try : 
                                    course['contentCourse'].remove(chapter)
                                except ValueError :
                                    msg = QMessageBox()
                                    msg.setWindowTitle("Warning")
                                    msg.setText("Vous n'avez" +        " pas sélectionné" +        " un chapitre")
                                    msg.setIcon(QMessageBox.Warning)
                                    ex = msg.exec_()
                        
        with open(self.__relPathToDatabase, 'w') as reWriteFile:
            json.dump(database, reWriteFile)

        self.__data = data
        self.buildTree()

    def edit(self):
        data = None
        itemSelected = ""
        itemSelectedType = ""
        selected = self.coursesView.selectedItems()
        for item in selected : 
            itemSelected = item.text(0)
            if self.coursesView.indexOfTopLevelItem(item) < 0 :
                itemSelectedType = "chapter"
            else : 
                itemSelectedType = "course"
        #ask user for course's name
        Dialog = QtWidgets.QDialog()
        ui = MyAddStructuralItemDialog()
        ui.setupUi(Dialog)
        ui.setContent("edit")
        Dialog.exec()
        
        action, name = ui.getInfos()

        if action == "cancel":
            return None
        with open(self.__relPathToDatabase, 'r') as  jsonFile:
            database = json.load(jsonFile)
        
        for globalData in database['globalData']:
            if globalData['username'] == self.__userName:
                for course in globalData['data']['courses']: 
                    if itemSelectedType == "course":
                        if course['name'] == itemSelected :
                            course['name'] = name
                    else : 
                        for chapter in course['contentCourse']:
                            if chapter['name'] == itemSelected :
                                chapter['name'] = name
                data = globalData['data']
        
        with open(self.__relPathToDatabase, 'w') as reWriteFile:
            json.dump(database, reWriteFile)

        self.__data = data
        self.buildTree()
        return action

    def preview(self):
        selected = self.coursesView.selectedItems()
        if len(selected) == 0 :
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Vous n\'avez sélectionné aucune section !")
            msg.setIcon(QMessageBox.Warning)
            ex = msg.exec_()
        elif selected[0].text(1) == "0":
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Vous ne pouvez pas afficher un aperçu de cette section car elle ne comporte aucune carte !")
            msg.setIcon(QMessageBox.Warning)
            ex = msg.exec_()
        else :
            itemSelectedType = ""
            for item in selected : 
                itemSelected = item.text(0)
                if self.coursesView.indexOfTopLevelItem(item) < 0 :
                    itemSelectedType = "chapter"
                else : 
                    itemSelectedType = "course"
            if itemSelectedType == "chapter":        
                self.__action = "preview_:_" + selected[0].parent().text(0) + "_:_" + selected[0].text(0)
            else : 
                self.__action = "preview_:_" + selected[0].text(0)
            self.dialog.done(0)

    def home(self):
        self.__action = "home"
        self.dialog.done(0)

    def getAction(self):
        return self.__action

    def buttonPressed(self, widget):
        widget.resize(0.95 * widget.width(), 0.95 * widget.height())
    
    def buttonReleased(self, widget):
        widget.resize((1/0.95) * widget.width(), (1/0.95) * widget.height())