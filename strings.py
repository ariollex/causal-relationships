import os
import pandas
import input_data
from calculations import replace_line

def setlanguage(language):
    global texts
    if language != open("current_language", 'r').read():
        replace_line("current_language", 0, language)
    texts = pandas.read_excel('languages/strings_' + language + '.xlsx')
    texts.columns = range(texts.columns.size)
    return


def changelanguage():
    files = os.listdir('languages')
    print('Available languages:')
    for i in range(len(files)):
        print(i + 1, ') ', files[i].replace('strings_', '').replace('.xlsx', ''), sep='')
    print('Please note that if the dataset and the program language are different, there may be errors.')
    print('Enter the number: ', end='')
    language = files[input_data.makeuserchoise(files)].replace('strings_', '').replace('.xlsx', '')
    setlanguage(language)


def printlanguage(line, column):
    return texts[line][column]