from strings import changelanguage, printlanguage


def makeuserchoise(list):
    while True:
        choise = input()
        if choise == 'L':
            changelanguage()
            return -2
        elif not choise.isdigit():
            print(printlanguage(1, 1))
        elif not (0 < int(choise) < len(list) + 1):
            print(printlanguage(1, 1))
        else:
            choise = int(choise) - 1
            return choise
        return -1
