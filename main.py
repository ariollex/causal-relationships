import pandas
import numpy

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

formatcauses = []
info = []
userchoise = -1


def printinfo(info):
    print()
    for i in range(len(info)):
        print(*info[i])


def debuglist(list):
    print()
    for i in range(len(list)):
        print(list[i])


def debugdataset(dataset):
    print(dataset.head)
    print(dataset.shape)


# Дебаг датасета
# debugdataset(data)

# Список инцидентов
for i in range(0, data.shape[0]):
    if causes[i] != 0:
        schoolclass = str(parallel[i]) + letter[i]
        formatcauses.append([name[i], schoolclass])
# Дебаг списка
# debuglist(formatcauses)

for i in range(len(formatcauses)):
    print(i + 1, ') ', sep='', end='')
    print(*formatcauses[i])

print("Выберите нужный случай и введите его номер: ", end='')

while True:
    userchoise = input()
    if not userchoise.isdigit():
        print('Такого номера нет. Введите его заново: ')
    elif not (0 < int(userchoise) < len(formatcauses) + 1):
        print('Такого номера нет. Введите его заново: ')
    else:
        userchoise = int(userchoise) - 1
        break

print('Вы выбрали номер ', userchoise + 1, '. Учащийся: ', formatcauses[userchoise][0], sep='')

for i in range(len(formatcauses)):
    if formatcauses[userchoise][1] == formatcauses[i][1] and userchoise != i:
        info.append(['Случай связан с', formatcauses[i][1], 'классом'])
        break

printinfo(info)
