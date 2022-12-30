import pandas
import numpy
import input_data
import calculations
import print_data
import charts
from strings import printlanguage, setlanguage

# Версия
version = '0.0.1-debug-closed'

# Язык
language = open("current_language", 'r').read()
setlanguage(language)
print(printlanguage(1, 15), version)
print('If you want to close the program, press "E"', end='\n\n')
print('Current language: ', language, '. If you want to change the language, enter L at any time.', sep='', end='\n\n')

# Датасет
file_loc = 'Dataset/Cause-effect-pairs-in-school.xlsx'
data = pandas.read_excel(file_loc)
data.columns = range(data.columns.size)
data.replace(numpy.nan, 0, inplace=True)

# Настройки датасета
name = data[0]
sex = data[1]
parallel = data[2]
letter = data[3]
causes = data[4]
infocauses = data[5]
timecauses = data[6]

# Список с выходными данными
info = []

# Другое
userchoise = -2
choisefunc = -2
graphs = [printlanguage(1, 5)]

# Выбор режима работы программы
functions = [printlanguage(1, 8), printlanguage(1, 9)]
while choisefunc == -2 or choisefunc == -1:
    if choisefunc == -2:
        print(printlanguage(1, 6) + ':')
        for i in range(len(functions)):
            print(i + 1, ') ', functions[i], sep='')
        print(printlanguage(1, 7) + ':', end=' ')
    choisefunc = input_data.makeuserchoise(functions)

# Вызов makeformatcauses для создания списка инцидентов
formatcauses = calculations.makeformatcauses(data, name, sex, parallel, letter, causes, infocauses, timecauses)

if choisefunc == 0:
    # Вызов функции makeuserchoise
    while userchoise == -2 or userchoise == -1:
        if userchoise == -2:
            print_data.printformatcauses(formatcauses)
        userchoise = input_data.makeuserchoise(formatcauses)

    print(printlanguage(1, 2), ' ', userchoise + 1, '. ' + printlanguage(2, 2) + ': ' if formatcauses[userchoise][1] == printlanguage(1, 4) or printlanguage(2, 3) == numpy.nan else '. ' + printlanguage(3, 2) + ': ', formatcauses[userchoise][0], sep='')

    # Вычисления
    calculations.intersection_of_classes(formatcauses, userchoise, info)

    # Вывод данных
    print_data.printinfo(info)

elif choisefunc == 1:
    print(printlanguage(1, 10) + ':')
    for i in range(len(graphs)):
        print(i + 1, ') ', graphs[i], sep='')
    print(printlanguage(1, 11) + ':', end=' ')
    choisegraph = input_data.makeuserchoise(functions)
    if choisegraph == 0:
        charts.graph_1(data, causes, formatcauses)