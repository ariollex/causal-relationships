import os
import numpy
import pandas
import input_data
from calculations import replace_line

language_texts = []


def set_language(language):
    global language_texts
    if language != open("current_language", 'r').read():
        replace_line("current_language", 0, language)
    language_texts = pandas.read_excel('languages/strings_' + language + '.xlsx')
    language_texts.replace(numpy.nan, 0, inplace=True)
    language_texts.columns = range(language_texts.columns.size)


def change_language():
    files = os.listdir('languages')
    print('Available languages:')
    for i in range(len(files)):
        print(i + 1, ') ', files[i].replace('strings_', '').replace('.xlsx', ''), sep='')
    print('Please note that if the dataset and the program language are different, there may be errors.')
    print('Enter the number: ', end='')
    language = -1
    while language == -1 or language == -2:
        language = input_data.make_user_choice(files)
    language = files[language].replace('strings_', '').replace('.xlsx', '')
    set_language(language)
    exit(print_on_language(1, 14))


def print_on_language(column, line):
    return language_texts[column][line]
