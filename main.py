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
    
    print(database)