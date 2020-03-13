# This Python file uses the following encoding: utf-8
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import myLogin_dialog as login
import myWarning_usr as warningUser
import myExplorer as explorer
import myCreateMenu as createMenu
import myCreateQACard as createQACard
import myAddCard
import myPreviewCards as previewCards
import json

def getUserData(database, userName):
    data = {}
    userExists = False
    for usersData in database['globalData']:
        if usersData['username'] == userName : 
            data = usersData['data']
            userExists = True
    return data, userExists

def loginUser(database, dbFile, prev_userName = ""): 
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = login.MyLoginDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()

    userName = ui.getUserName()
    del app
    del Dialog
    del ui
    data, userExists = getUserData(database, userName)

    while not userExists:
        #opening a new dialog => create user or not 
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = warningUser.MyWarningUserName()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
        createUser = ui.getChoice()
        del app
        del Dialog
        del ui

        if createUser:
            database['globalData'].append({'username' : userName, 'data' : {"courses" : []}}) 
            userExists = True
            data = {"courses" : []}
            with open(dbFile, 'w') as reWriteFile:
                json.dump(database, reWriteFile)
            
        else : 
            #go back to entering user name
            app = QtWidgets.QApplication(sys.argv)
            Dialog = QtWidgets.QDialog()
            ui = login.MyLoginDialog()
            ui.setupUi(Dialog)
            Dialog.show()
            app.exec_()
            userName = ui.getUserName()
            del app
            del Dialog
            del ui
            data, userExists = getUserData(database, userName)
    return data, userName

def openExplorer(data, dataBaseFile, userName, database):
    newUserName = userName
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = explorer.MyExplorer()
    ui.setupUi(Dialog, data)
    Dialog.show()
    app.exec_()
    action = ui.getAction()
    del app 
    del Dialog
    del ui
    if action == "logout":
        data, newUserName = loginUser(database, dataBaseFile, userName)
        openExplorer(data, dataBaseFile, newUserName, database)
    elif action == "create":
        openCreatePage(data, dataBaseFile, newUserName, database)
    elif action == "study":
        pass
    return action, data
    
def openCreatePage(data, dataBaseFile, userName, database):
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = createMenu.MyCreatePageDialog()
    ui.setupUi(Dialog, data, databaseFile, userName)
    Dialog.show()
    app.exec_()
    action = ui.getAction()
    del app 
    del Dialog
    del ui
    if action == "home":
        database = {}
        with open(databaseFile, 'r') as  json_file:
            database = json.load(json_file)
        data = getUserData(database, userName)[0]
        openExplorer(data, dataBaseFile, userName,                   database)
    elif "addCard" in action :
        parsedAction = action.split("_:_")
        course = parsedAction[1]
        chapter = parsedAction[2]
        resp, cardData = addCard(data, dataBaseFile, userName,                           database, course, chapter)
        '''
        if cardData[0] == "confirm" : 
            print("confirm")
            msg = QMessageBox()
            msg.setWindowTitle("Good job")
            msg.setText("Vous avez créé une carte dans le chapitre {} avec comme question {} et comme réponse {}".format(chapter, cardData[1][1], cardData[1][2]))
            msg.setIcon(QMessageBox.Information)
            ex = msg.exec_()
        elif cardData[0] == "cancel":
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Vous avez annulé la création de votre carte")
            msg.setIcon(QMessageBox.Information)
            ex = msg.exec_()
        '''
        print("reouvre createpage")
        database = {}
        with open(databaseFile, 'r') as  json_file:
            database = json.load(json_file)
        data = getUserData(database, userName)[0]
        openCreatePage(data, dataBaseFile, userName, database)
    elif "preview" in action:
        parsedAction = action.split("_:_")
        course = parsedAction[1]
        if len(parsedAction) > 2: #specific chapter
            chapter = parsedAction[2]
            preview(data, dataBaseFile, course, userName, database, chapter)
        elif len(parsedAction) == 2: #whole course
            preview(data, dataBaseFile, course, userName, database)
        else : 
            print("Error while parsing action")
    return action, data

def addCard(data, dataBaseFile, userName,               database, course, chapter) :
    action = ""
    data = None
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = myAddCard.MyAddCardDialog()
    ui.setupUi(Dialog, chapter)
    Dialog.show()
    app.exec_()
    action = ui.getAction()
    del app 
    del Dialog
    del ui
    if action == "Classique":
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = createQACard.MyCreateQACard()
        ui.setupUi(Dialog, dataBaseFile, course, chapter,      userName)
        Dialog.show()
        app.exec_()
        button, question, answer = ui.getInfos()
        data = button, question, answer
        del app 
        del Dialog
        del ui
    else : 
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Cette fonctionnalité n\'existe pas" +              " encore :-(")
        msg.setIcon(QMessageBox.Information)
        ex = msg.exec_()
    return action, data 

def preview(data, databaseFile, course, userName, database, chapter=None):
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = previewCards.MyPreviewCards()
    ui.setupUi(Dialog, data, databaseFile, course, userName, chapter)
    Dialog.show()
    app.exec_()
    action = ui.getAction()
    del app 
    del Dialog
    del ui
    if action  == 'stop':
        with open(databaseFile, 'r') as  json_file:
            database = json.load(json_file)
        data, userExists = getUserData(database, userName)
        if userExists:
            openCreatePage(data, databaseFile, userName, database)
        else : 
            sys.exit(-1)

if __name__ == "__main__":
    database = ""
    databaseFile = 'data' + os.path.sep + 'data.json'
    with open(databaseFile, 'r') as  json_file:
        database = json.load(json_file)
    totalPath =  os.path.abspath(os.getcwd()).split(os.path.sep)
    backupPath = totalPath [0] + os.path.sep + totalPath[1] + os.path.sep  + totalPath[2] + os.path.sep
    try :
        with open(backupPath +'SC_backupBefore.json', 'w') as json_write :
            json.dump(database, json_write)
    except : 
        print("Wrong backup path !")
        sys.exit(-1)
    #print(backupPath)
    data, userName = loginUser(database, databaseFile)
    
    openExplorer(data, databaseFile, userName, database)
    with open(databaseFile, 'r') as  json_file:
        database = json.load(json_file)
    try :
        with open(backupPath + 'SC_backupAfter.json', 'w') as json_write :
            json.dump(database, json_write)
    except : 
        print("Wrong backup path !")
        sys.exit(-1)