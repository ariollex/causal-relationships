import strings


def makeformatcauses(data, name, sex, parallel, letter, causes, infocauses, timecauses):
    formatcauses = []
    for i in range(0, data.shape[0]):
        if causes[i] != 0:
            schoolclass = str(parallel[i]) + ' "' + letter[i] + '"'
            formatcauses.append([name[i], sex[i], schoolclass, timecauses[i], infocauses[i]])
    return formatcauses


def intersection_of_classes(formatcauses, userchoise, info):
    for i in range(len(formatcauses)):
        if formatcauses[userchoise][2] == formatcauses[i][2] and userchoise != i:
            info.append([strings.printlanguage(1, 3), formatcauses[i][2], strings.printlanguage(2, 3)])
            break


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()