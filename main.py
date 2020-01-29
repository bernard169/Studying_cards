# This Python file uses the following encoding: utf-8
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mylogin_dialog as login
import myWarning_usr as warningUser
import Card 
import Chapter
import Course
import json

def getUserData(database, userName):
    data = {}
    userExists = False
    for usersData in database['globalData']:
        if usersData['username'] == userName : 
            data = usersData['data']
            userExists = True
    return data, userExists

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = login.MyLoginDialog()
    ui.setupUi(Dialog)
    Dialog.show()

    database = ""
    with open('data.json', 'r') as  json_file:
        database = json.load(json_file)

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
            database['globalData'].append({'username' : userName, 'data' : {}}) 
            userExists = True
            
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
    print(data)
    print(userExists)
