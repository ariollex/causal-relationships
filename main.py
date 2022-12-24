import pandas

# Датасет
file_loc = 'Dataset/Cause-effect-pairs-in-school.xlsx'
data = pandas.read_excel(file_loc)

# Настройки датасета
name = data.Имя
parallel = data.Параллель
letter = data.Буква
causes = data.Инцидент

formatcauses = []
info = []
userchoise = -1

def printinfo(info):
    for i in range(len(info)):
        print(*info[i])

def debuglist(list):
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
    print(i + 1,') ', sep='', end='')
    print(*formatcauses[i])

print("Выберите нужный случай и введите его номер: ", end='')

while not(-1 < userchoise < len(formatcauses)):
    userchoise = int(input()) - 1
    if not(-1 < userchoise < len(formatcauses)):
        print('Такого номера нет. Введите его заново: ')

print()
print('Вы выбрали номер ', userchoise + 1, '. Учащийся: ', formatcauses[userchoise][0], sep='')
print()

for i in range(len(formatcauses)):
    if formatcauses[userchoise][1] == formatcauses[i][1] and userchoise != i:
        info.append(['Случай связан с', formatcauses[i][1], 'классом'])
        break

printinfo(info)