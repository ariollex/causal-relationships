import pandas
import numpy
import matplotlib.pyplot
import input_data
import calculations
import print_data
from strings import printlanguage, setlanguage
import debug

version = '0.0.1-debug-closed'
print('Causal relationships in school, ver', version)
print('If you want to close the program, press "E"', end='\n\n')

# Язык
language = open("current_language", 'r').read()
print('Current language: ', language, '. If you want to change the language, enter L at any time.', sep='', end='\n\n')
setlanguage(language)

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

# Вызов makeformatcauses для создания списка инцидентов
formatcauses = calculations.makeformatcauses(data, name, sex, parallel, letter, causes, infocauses, timecauses)

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