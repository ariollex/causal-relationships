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
data.replace(numpy.nan, 0, inplace=True)

# Настройки датасета
name = data['Имя']
parallel = data['Параллель']
letter = data['Буква']
causes = data['Инцидент']
infocauses = data['Информация об инцидентах']
timecauses = data['Время инцидента']

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