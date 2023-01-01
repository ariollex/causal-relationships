import strings


def make_list_incidents(data, name, sex, parallel, letter, causes, info_about_causes, time_causes):
    example_list_incidents = []
    for i in range(0, data.shape[0]):
        if causes[i] != 0:
            school_class = str(parallel[i]) + ' "' + letter[i] + '"'
            example_list_incidents.append([name[i], sex[i], school_class, time_causes[i], info_about_causes[i]])
    return example_list_incidents


def intersection_of_classes(example_list_incidents, user_selection, info):
    for i in range(len(example_list_incidents)):
        if example_list_incidents[user_selection][2] == example_list_incidents[i][2] and user_selection != i:
            info.append(
                [strings.print_on_language(1, 3), example_list_incidents[i][2], strings.print_on_language(2, 3)])
            break


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
