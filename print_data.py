def printinfo(info):
    print()
    for i in range(len(info)):
        print(*info[i])


def printformatcauses(formatcauses):
    for i in range(len(formatcauses)):
        print(i + 1, ') ', sep='', end='')
        print(*formatcauses[i])

    print("Выберите нужный случай и введите его номер: ", end='')
