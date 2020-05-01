from PyQt5 import QtCore, QtGui, QtWidgets

def formatText(menu, textWidget):
    index = menu.currentIndex()
    cursor = textWidget.textCursor()#QtGui.QTextCursor()
    fmt = cursor.charFormat()
    font = textWidget.currentFont()
    color = fmt.foreground().color()
    backgroundColor = fmt.background().color()
    noBackground = True
    if index is 1 :
        font.setBold(True)
    elif index is 2:
        font.setUnderline(True)
    elif index is 3:
        font.setItalic(True)
    elif index is 4:
        font.setStrikeOut(True)
    elif index is 5 :
        backgroundColor.setNamedColor("yellow")
        noBackground = False
    elif index is 6 : 
        color.setNamedColor("red")
    elif index is 7 : 
        color.setNamedColor("green")
    elif index is 8 : 
        color.setRgb(188, 91, 255) #purple
    elif index is 0 :
        color.setNamedColor("black")
        font.setBold(False)
        font.setUnderline(False)
        font.setItalic(False)
        font.setStrikeOut(False)
    brush = QtGui.QBrush(color)
    fmt.setFont(font)
    fmt.setForeground(brush)
    if not noBackground :
        backgroundBrush = QtGui.QBrush(backgroundColor)
        fmt.setBackground(backgroundBrush)
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
        if fmt.fontWeight() > 50:  #normal weight is 50, greater weight means bolded text
            specialFormatsQ[i].append('b')
        if fmt.foreground().color().red() > 200:
            specialFormatsQ[i].append('r')
        if fmt.foreground().color().green() > 120:
            specialFormatsQ[i].append('g')
        if fmt.foreground().color().yellow() > 200:
            specialFormatsQ[i].append('h')
        if (fmt.foreground().color().red() > 180) and (fmt.foreground().color().blue() > 200):
            print('purple')
            specialFormatsQ[i].append('p')
        print ("red :")
        print(fmt.foreground().color().red())
        print("blue : ")
        print(fmt.foreground().color().blue())
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
        if fmt.fontWeight() > 50:  #normal weight is 50, greater weight means bolded text
            specialFormatsA[i].append('b')
        if fmt.foreground().color().red() > 200:
            specialFormatsA[i].append('r')
        if fmt.foreground().color().green() > 120:
            specialFormatsA[i].append('g')
        if fmt.background().color().yellow() > 200:
            specialFormatsA[i].append('h')
        if (fmt.foreground().color().red() > 180) and (fmt.foreground().color().blue() > 200):
            specialFormatsA[i].append('p')
        i += 1 
    #remove and count the number of following empty lists
    noFormatCharsQCounter = 0
    fmtQ = []
    for spFormat in specialFormatsQ : 
        if len(spFormat) is not 0:
            if noFormatCharsQCounter is not 0 :
                fmtQ.append(noFormatCharsQCounter)
                noFormatCharsQCounter = 0
            fmtQ.append(spFormat)
        else : 
            noFormatCharsQCounter += 1
    
    noFormatCharsACounter = 0
    fmtA = []
    for spFormat in specialFormatsA : 
        if len(spFormat) is not 0:
            if noFormatCharsACounter is not 0 :
                fmtA.append(noFormatCharsACounter)
                noFormatCharsACounter = 0
            fmtA.append(spFormat)
        else : 
            noFormatCharsACounter += 1

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
    return fmtQ, fmtA, noFormatQ, noFormatA

def getFormat(questionWidget, formatQ, answerWidget=None, formatA=None):
    cursorQ = questionWidget.textCursor()
    cursorQ.movePosition(QtGui.QTextCursor.Start)
    i = 0
    while i < len(formatQ):
        cursorQ.movePosition(QtGui.QTextCursor.NextCharacter, mode=QtGui.QTextCursor.KeepAnchor) 
        totalCharacterFormat = QtGui.QTextCharFormat()
        font = questionWidget.currentFont()
        color = QtGui.QColor()
        bckground = QtGui.QColor()
        noBckground = True
        noColor = True
        fmtCaracter = formatQ[i]
        if type(fmtCaracter) is list:
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
                    noColor = False
                elif fmt is 'g':
                    color.setNamedColor("green")
                    noColor = False
                elif fmt is 'h':
                    bckground.setNamedColor("yellow")
                    noBckground = False
                elif fmt is 'p':
                    color.setRgb(188, 91, 255)
                    noColor = False
            totalCharacterFormat.setFont(font)
            if not noColor:
                brush = QtGui.QBrush(color)
                totalCharacterFormat.setForeground(brush)
            if not noBckground:
                brush = QtGui.QBrush(bckground)
                totalCharacterFormat.setBackground(brush)
            cursorQ.setCharFormat(totalCharacterFormat)
            cursorQ.movePosition(QtGui.QTextCursor.NextCharacter) #reset anchor to get a single character at each iteration
        elif type(fmtCaracter) is int:
            counter = 0
            while counter < fmtCaracter : 
                cursorQ.movePosition(QtGui.QTextCursor.NextCharacter)
                counter += 1
        i += 1
    if answerWidget is not None:
        cursorA = answerWidget.textCursor()
        cursorA.movePosition(QtGui.QTextCursor.Start)
        i = 0
        while i < len(formatA):
            cursorA.movePosition(QtGui.QTextCursor.NextCharacter, mode=QtGui.QTextCursor.KeepAnchor)
            totalCharacterFormat = QtGui.QTextCharFormat()
            font = answerWidget.currentFont()
            fmtCaracter = formatA[i]
            color = QtGui.QColor()
            noColor = True
            bckground = QtGui.QColor()
            noBckground = True
            if type(fmtCaracter) is list:
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
                        noColor = False
                    elif fmt is 'g':
                        color.setNamedColor("green")
                        noColor = False
                    elif fmt is 'h':
                        bckground.setNamedColor("yellow")
                        noBckground = False
                    elif fmt is 'p':
                        color.setRgb(188, 91, 255)
                        noColor = False
                totalCharacterFormat.setFont(font)
                if not noColor:
                    brush = QtGui.QBrush(color)
                    totalCharacterFormat.setForeground(brush)
                if not noBckground:
                    brush = QtGui.QBrush(bckground)
                    totalCharacterFormat.setBackground(brush)
                cursorA.setCharFormat(totalCharacterFormat)
                cursorA.movePosition(QtGui.QTextCursor.NextCharacter)
            elif type(fmtCaracter) is int:
                counter = 0
                while counter < fmtCaracter : 
                    cursorA.movePosition(QtGui.QTextCursor.NextCharacter)
                    counter += 1
            i += 1
    
def buttonPressed(widget):
    widget.resize(0.95 * widget.width(), 0.95 * widget.height())

def buttonReleased(widget):
    widget.resize((1/0.95) * widget.width(), (1/0.95) * widget.height())