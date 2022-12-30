from strings import changelanguage, printlanguage


def makeuserchoise(list):
    while True:
        choise = input()
        if choise == 'E':
            exit()
        elif choise == 'L':
            changelanguage()
            return -2
        elif not choise.isdigit():
            print(printlanguage(1, 1), end=': ')
        elif not (0 < int(choise) < len(list) + 1):
            print(printlanguage(1, 1), end=': ')
        else:
            choise = int(choise) - 1
            return choise
        return -1
