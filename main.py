import pandas
import numpy
import matplotlib.pyplot
import input_data
import calculations
import print_data
import strings
import debug

# Язык
language = 'ru-RU'
strings.setlanguage(language)

# Датасет
file_loc = 'Dataset/Cause-effect-pairs-in-school.xlsx'
data = pandas.read_excel(file_loc)
data.columns = range(data.columns.size)
data.replace(numpy.nan, 0, inplace=True)

# Настройки датасета
name = data[0]
parallel = data[2]
letter = data[3]
causes = data[4]
infocauses = data[5]
timecauses = data[6]

# Список с выходными данными
info = []

# Вызов makeformatcauses для создания списка инцидентов
formatcauses = calculations.makeformatcauses(data, name, parallel, letter, causes, infocauses, timecauses)

# Вызов функции makeuserchoise
userchoise = input_data.makeuserchoise(formatcauses)

# Вычисления
calculations.intersection_of_classes(formatcauses, userchoise, info)

# Вывод данных
print_data.printinfo(info)