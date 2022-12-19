import pandas
file_loc = 'Dataset/Cause-effect-pairs-in-school.csv'
data = pandas.read_csv(file_loc)
formatcauses = []

# Дебаг датасета
# print(data.head)

# Создание и заполнение массива causes, в котором указаны все случаи в школе в период времени, указанный в таблице
for i in range(0, data.shape[0]): # пробег по всей таблице
    if data.causes[i] != 0: # Поиск случаев. Если случай найден, то:
        schoolclass = str(data.parallel[i]) + data.letter[i] # Определение класса
        formatcauses.append([data.name[i], schoolclass, data.causes[i]]) # Присваивание массива с именем, классом и случаем в массив causes

# Дебаг массива
for i in range(len(formatcauses)):
    print(formatcauses[i])
print(len(formatcauses))