import pandas
file_loc = 'Dataset/Cause-effect-pairs-in-school.csv'
data = pandas.read_csv(file_loc)
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
    if data.causes[i] != 0: # Поиск случаев. Если случай найден, то:
        schoolclass = str(data.parallel[i]) + data.letter[i] # Определение класса
        formatcauses.append([data.name[i], schoolclass]) # Присваивание массива с именем и классом в массив causes
# Дебаг массива
# debuglist(formatcauses)

for i in range(len(formatcauses)):
    print(i+1, formatcauses[i])
print("Выберите нужный случай и введите его номер: ", end='')
userchoise = int(input()) - 1
print()
print('Вы выбрали номер ', userchoise, '. Случай связан с учеником по имени ', formatcauses[userchoise][0], sep='')
print()

for i in range(len(formatcauses)):
    if formatcauses[userchoise][1] == formatcauses[i][1] and userchoise != i:
        info.append(['Случай напрямую связан с', formatcauses[i][1], 'классом'])
        break

printinfo(info)