import os
import numpy
import pandas
import input_data
from calculations import replace_line


def setlanguage(language):
    global texts
    if language != open("current_language", 'r').read():
        replace_line("current_language", 0, language)
    texts = pandas.read_excel('languages/strings_' + language + '.xlsx')
    texts.replace(numpy.nan, 0, inplace=True)
    texts.columns = range(texts.columns.size)


def changelanguage():
    files = os.listdir('languages')
    print('Available languages:')
    for i in range(len(files)):
        print(i + 1, ') ', files[i].replace('strings_', '').replace('.xlsx', ''), sep='')
    print('Please note that if the dataset and the program language are different, there may be errors.')
    print('Enter the number: ', end='')
    language = -1
    while language == -1 or language == -2:
        language = input_data.makeuserchoise(files)
    language = files[language].replace('strings_', '').replace('.xlsx', '')
    setlanguage(language)
    exit(printlanguage(1, 14))


def printlanguage(line, column):
    return texts[line][column]
