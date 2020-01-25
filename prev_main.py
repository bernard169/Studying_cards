import os
import sys
import Card 
import Chapter
import Course
import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class testQTMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(testQTMain, self).__init__()
        loadUi('mainwindow.ui', self)
        # call __init__(self) of the custom base class here

def getUserData(database, userName):
    data = {}
    userExists = False
    for usersData in database['globalData']:
        if usersData['username'] == userName : 
            data = usersData['data']
            userExists = True
    return data, userExists
    
if __name__ == '__main__' :
    database = ""
    with open('data.json', 'r') as  json_file:
        database = json.load(json_file)
    print(database)

    userName = input("What is your username ?\n")
    data, userExists = getUserData(database, userName)
    
    while not userExists:
        choiceCreate = input("The username you entered " +
                            "\"{}\" do not ".format(userName) + 
                            "exist. Do you want to create a new user?" +
                            " Y/n \n")
        if choiceCreate == "n":
            userName = input("What is your username ?\n")
            data, userExists = getUserData(database, userName)
        else : 
            database['globalData'].append({'username' : userName, 
                                            'data' : {}}) 
            userExists = True
    
    app = QtWidgets.QApplication(sys.argv)
    window = testQTMain()
    window.show()
    sys.exit(app.exec_())