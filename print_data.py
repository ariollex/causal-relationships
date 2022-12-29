from strings import printlanguage


def printinfo(info):
    print()
    for i in range(len(info)):
        print(*info[i])


def printformatcauses(formatcauses):
    for i in range(len(formatcauses)):
        print(i + 1, ') ', sep='', end='')
        print(*formatcauses[i][0], ' ', *formatcauses[i][2], sep='')
    print(printlanguage(1, 0), end='')
