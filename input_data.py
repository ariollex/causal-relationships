import print_data
import strings

def makeuserchoise(formatcauses):
    print_data.printformatcauses(formatcauses)
    while True:
        userchoise = input()
        if not userchoise.isdigit():
            print(strings.printlanguage(1, 1))
        elif not (0 < int(userchoise) < len(formatcauses) + 1):
            print(strings.printlanguage(1, 1))
        else:
            userchoise = int(userchoise) - 1
            break
    print(strings.printlanguage(1, 2), userchoise + 1, strings.printlanguage(2, 2) if formatcauses[userchoise][1] == strings.printlanguage(1, 4) else strings.printlanguage(3, 2), formatcauses[userchoise][0], sep='')
    return userchoise
