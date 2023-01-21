from strings import print_on_language


def print_info(info):
    print()
    for i in range(len(info)):
        print(*info[i])


def print_list_incidents(example_list_incidents):
    for i in range(len(example_list_incidents)):
        print(i + 1, ') ', sep='', end='')
        print(*example_list_incidents[i][0], ' ', *example_list_incidents[i][2], sep='')
    print(print_on_language(1, 0), end=': ')


def print_selection_list(example_list):
    for i in range(len(example_list)):
        print(i + 1, ') ', example_list[i], sep='')


def is_fight(in_class, count_participants, count_participants_in_class, student_class, suspicious, maximum):
    # result = strings.print_on_language(1, 22) + ' :'
    # if in_class == 0:
    #     result = result + strings.print_on_language(1, 23).lower()
    #     if suspicious != 0:
    #         result = result + strings.print_on_language(1, 24) + ' ' + maximum[1] + ' ' + strings.print_on_language(2, 24) + ' ' maximum[0] + ' ' + print_on_language(3, 24)
    # else:
    #     result = strings.print_on_language(1, 23).lower() + strings.print_on_language(2, 23)
    #     if suspicious != 0:
    #         result = result + strings.print_on_language(1, 24) + ' ' + maximum[1] + ' ' + strings.print_on_language(2, 24) + ' ' maximum[0] + ' ' + print_on_language(3, 24)
    # return result
    print('ЭТО ДРАКА')


def is_incident_in_classroom(count_participants_in_class, student_class, suspicious, maximum):
    print('ЭТО СЛУЧАЙ В КЛАССЕ БЕЗ ВРЕМЕНИ')


def is_personal_incident():
    print('ЭТО ПЕРСОНАЛЬНЫЙ СЛУЧАЙ')
