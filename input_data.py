from strings import change_language, print_on_language


def make_user_choice(example_list):
    while True:
        choice = input()
        if choice == 'E':
            exit()
        elif choice == 'L':
            change_language()
            return -2
        elif not choice.isdigit():
            print(print_on_language(1, 1), end=': ')
        elif not (0 < int(choice) < len(example_list) + 1):
            print(print_on_language(1, 1), end=': ')
        else:
            choice = int(choice) - 1
            return choice
        return -1
