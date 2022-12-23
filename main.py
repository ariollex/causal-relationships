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

# Создание и заполнение массива causes, в котором указаны все случаи в школе в период времени, указанный в таблице
for i in range(0, data.shape[0]): # пробег по всей таблице
    if causes[i] != 0: # Поиск случаев. Если случай найден, то:
        schoolclass = str(parallel[i]) + letter[i] # Определение класса
        formatcauses.append([name[i], schoolclass]) # Присваивание массива с именем и классом в массив causes
# Дебаг массива
# debuglist(formatcauses)

for i in range(len(formatcauses)):
    print(i + 1,') ', sep='', end='')
    print(*formatcauses[i])

print("Выберите нужный случай и введите его номер: ", end='')
userchoise = int(input()) - 1
print()
print('Вы выбрали номер ', userchoise + 1, '. Учащийся: ', formatcauses[userchoise][0], sep='')
print()

for i in range(len(formatcauses)):
    if formatcauses[userchoise][1] == formatcauses[i][1] and userchoise != i:
        info.append(['Случай связан с', formatcauses[i][1], 'классом'])
        break

printinfo(info)