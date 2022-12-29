import pandas

def setlanguage(language):
    global texts, variable
    texts = pandas.read_excel('languages/strings_' + language + '.xlsx')
    texts.columns = range(texts.columns.size)

def printlanguage(line, column):
    return texts[line][column]