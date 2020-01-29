# This Python file uses the following encoding: utf-8
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mylogin_dialog as login
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
    
    userName = ui.getUserName()
    data, userExists = getUserData(database, userName)
    
    
    sys.exit(app.exec_())
    userName = ui.getUserName()
    print(data, userExists)
