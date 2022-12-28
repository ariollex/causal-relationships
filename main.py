import pandas
import numpy
import input_data
import calculations
import print_data
import debug

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

# Ввод данных
# Вызов makeformatcauses для создания списка инцидентов
formatcauses = input_data.makeformatcauses(data, name, parallel, letter, causes, infocauses, timecauses)
# Вызов функции makeuserchoise
userchoise = input_data.makeuserchoise(formatcauses)

# Вычисления
calculations.intersection_of_classes(formatcauses, userchoise, info)

# Вывод данных
print_data.printinfo(info)