def makeuserchoise(formatcauses):
    userchoise = -1
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
    return userchoise