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
        backgroundColor.setNamedColor("transparent")
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

def addFormat(textWidget, text):
    i = 0
    fmt = QtGui.QTextCharFormat()
    cursor = textWidget.textCursor()
    cursor.movePosition(QtGui.QTextCursor.Start)
    specialFormats = []
    while i < len(text): 
        specialFormats.append([])
        cursor.movePosition(QtGui.QTextCursor.NextCharacter)
        fmt = cursor.charFormat()
        if fmt.fontUnderline():
            specialFormats[i].append('u')
        if fmt.fontItalic():
            specialFormats[i].append('i')
        if fmt.fontStrikeOut():
            specialFormats[i].append('s')
        if fmt.fontWeight() > 50:  #normal weight is 50, greater weight means bolded text
            specialFormats[i].append('b')
        if fmt.foreground().color().red() > 200:
            specialFormats[i].append('r')
        if fmt.foreground().color().green() > 120:
            specialFormats[i].append('g')
        if fmt.background().color().yellow() > 200:
        #if fmt.foreground().color().yellow() > 200:
            specialFormats[i].append('h')
        if (fmt.foreground().color().red() > 180) and (fmt.foreground().color().blue() > 200):
            print('purple')
            specialFormats[i].append('p')
        print ("red :")
        print(fmt.foreground().color().red())
        print("blue : ")
        print(fmt.foreground().color().blue())
        i += 1 
   
    #remove and count the number of following empty lists
    noFormatCharsCounter = 0
    fmt = []
    for spFormat in specialFormats : 
        if len(spFormat) is not 0:
            if noFormatCharsCounter is not 0 :
                fmt.append(noFormatCharsCounter)
                noFormatCharsCounter = 0
            fmt.append(spFormat)
        else : 
            noFormatCharsCounter += 1

    noFormat = False
    for l in specialFormats : 
        if len(l) is not 0 : 
            noFormat = False
            break
        else :
            noFormat = True 
    return fmt, noFormat

def getFormat(textWidget, formatText):
    cursor = textWidget.textCursor()
    cursor.movePosition(QtGui.QTextCursor.Start)
    i = 0
    while i < len(formatText):
        cursor.movePosition(QtGui.QTextCursor.NextCharacter, mode=QtGui.QTextCursor.KeepAnchor) 
        totalCharacterFormat = QtGui.QTextCharFormat()
        font = textWidget.currentFont()
        color = QtGui.QColor()
        bckground = QtGui.QColor()
        noBckground = True
        noColor = True
        fmtCaracter = formatText[i]
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
            cursor.setCharFormat(totalCharacterFormat)
            cursor.movePosition(QtGui.QTextCursor.NextCharacter) #reset anchor to get a single character at each iteration
        elif type(fmtCaracter) is int:
            counter = 0
            while counter < fmtCaracter : 
                cursor.movePosition(QtGui.QTextCursor.NextCharacter)
                counter += 1
        i += 1
    
def buttonPressed(widget):
    widget.resize(0.95 * widget.width(), 0.95 * widget.height())

def buttonReleased(widget):
    widget.resize((1/0.95) * widget.width(), (1/0.95) * widget.height())