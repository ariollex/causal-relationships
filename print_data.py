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
