from PyQt5 import QtCore, QtGui, QtWidgets

def formatText(menu, textWidget):
    index = menu.currentIndex()
    cursor = textWidget.textCursor()#QtGui.QTextCursor()
    fmt = cursor.charFormat()
    font = textWidget.currentFont()
    color = fmt.foreground().color()
    if index is 1 :
        font.setBold(True)
    elif index is 2:
        font.setUnderline(True)
    elif index is 3:
        font.setItalic(True)
    elif index is 4:
        font.setStrikeOut(True)
    elif index is 5 : 
        color.setNamedColor("red")
    elif index is 6 : 
        color.setNamedColor("green")
    elif index is 0 :
        color.setNamedColor("black")
        font.setBold(False)
        font.setUnderline(False)
        font.setItalic(False)
        font.setStrikeOut(False)
    brush = QtGui.QBrush(color)
    fmt.setFont(font)
    fmt.setForeground(brush)
    cursor.setCharFormat(fmt)

def addFormat(questionWidget, answerWidget, question, answer):
    i = 0
    fmt = QtGui.QTextCharFormat()
    cursorQ = questionWidget.textCursor()
    cursorQ.movePosition(QtGui.QTextCursor.Start)
    specialFormatsQ = []
    while i < len(question): 
        specialFormatsQ.append([])
        cursorQ.movePosition(QtGui.QTextCursor.NextCharacter)
        fmt = cursorQ.charFormat()
        if fmt.fontUnderline():
            specialFormatsQ[i].append('u')
        if fmt.fontItalic():
            specialFormatsQ[i].append('i')
        if fmt.fontStrikeOut():
            specialFormatsQ[i].append('s')
        if fmt.fontWeight() > 50:  #normal weight is 50, greater means bolded text
            specialFormatsQ[i].append('b')
        if fmt.foreground().color().red() > 200:
            specialFormatsQ[i].append('r')
        if fmt.foreground().color().green() > 120:
            specialFormatsQ[i].append('g')
        i += 1 
    i = 0
    cursorA = answerWidget.textCursor()
    cursorA.movePosition(QtGui.QTextCursor.Start)
    specialFormatsA = []
    while i < len(answer): 
        specialFormatsA.append([])
        cursorA.movePosition(QtGui.QTextCursor.NextCharacter)
        fmt = cursorA.charFormat()
        if fmt.fontUnderline():
            specialFormatsA[i].append('u')
        if fmt.fontItalic():
            specialFormatsA[i].append('i')
        if fmt.fontStrikeOut():
            specialFormatsA[i].append('s')
        if fmt.fontWeight() > 50:  #normal weight is 50, greater means bolded text
            specialFormatsA[i].append('b')
        if fmt.foreground().color().red() > 200:
            specialFormatsA[i].append('r')
        if fmt.foreground().color().green() > 120:
            specialFormatsA[i].append('g')
        i += 1 
    noFormatQ = False
    for l in specialFormatsQ : 
        if len(l) is not 0 : 
            noFormatQ = False
            break
        else :
            noFormatQ = True
    noFormatA = False
    for l in specialFormatsA : 
        if len(l) is not 0 : 
            noFormatA = False
            break
        else :
            noFormatA = True    
    return specialFormatsQ, specialFormatsA, noFormatQ, noFormatA

def getFormat(questionWidget, answerWidget, formatQ, formatA):
    cursorQ = questionWidget.textCursor()
    cursorQ.movePosition(QtGui.QTextCursor.Start)
    i = 0
    while i < len(formatQ):
        cursorQ.movePosition(QtGui.QTextCursor.NextCharacter, mode=QtGui.QTextCursor.KeepAnchor) 
        totalCharacterFormat = QtGui.QTextCharFormat()
        font = questionWidget.currentFont()
        color = QtGui.QColor()
        fmtCaracter = formatQ[i]
        for fmt in fmtCaracter :
            if fmt is 'b':
                font.setBold(True)
            elif fmt is 'u':
                font.setUnderline(True)
            elif fmt is 'i':
                font.setItalic(True)
            elif fmt is 's':
                font.setStrikeOut(True)
            elif fmt is 'r':
                color.setNamedColor("red")
            elif fmt is 'g':
                color.setNamedColor("green")
        brush = QtGui.QBrush(color)
        totalCharacterFormat.setFont(font)
        totalCharacterFormat.setForeground(brush)
        cursorQ.setCharFormat(totalCharacterFormat)
        cursorQ.movePosition(QtGui.QTextCursor.NextCharacter) #reset anchor to get a single character at each iteration
        i += 1
    cursorA = answerWidget.textCursor()
    cursorA.movePosition(QtGui.QTextCursor.Start)
    i = 0
    while i < len(formatA):
        cursorA.movePosition(QtGui.QTextCursor.NextCharacter, mode=QtGui.QTextCursor.KeepAnchor)
        totalCharacterFormat = QtGui.QTextCharFormat()
        font = answerWidget.currentFont()
        fmtCaracter = formatA[i]
        color = QtGui.QColor()
        for fmt in fmtCaracter :
            if fmt is 'b':
                font.setBold(True)
            elif fmt is 'u':
                font.setUnderline(True)
            elif fmt is 'i':
                font.setItalic(True)
            elif fmt is 's':
                font.setStrikeOut(True)
            elif fmt is 'r':
                color.setNamedColor("red")
            elif fmt is 'g':
                color.setNamedColor("green")
        brush = QtGui.QBrush(color)
        totalCharacterFormat.setFont(font)
        totalCharacterFormat.setForeground(brush)
        cursorA.setCharFormat(totalCharacterFormat)
        cursorA.movePosition(QtGui.QTextCursor.NextCharacter)
        i += 1