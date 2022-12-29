import strings


def makeformatcauses(data, name, parallel, letter, causes, infocauses, timecauses):
    formatcauses = []
    for i in range(0, data.shape[0]):
        if causes[i] != 0:
            schoolclass = str(parallel[i]) + letter[i]
            formatcauses.append([name[i], schoolclass, timecauses[i], infocauses[i]])
    return formatcauses


def intersection_of_classes(formatcauses, userchoise, info):
    for i in range(len(formatcauses)):
        if formatcauses[userchoise][1] == formatcauses[i][1] and userchoise != i:
            info.append([strings.printlanguage(1, 3), formatcauses[i][1], strings.printlanguage(2, 3)])
            break
