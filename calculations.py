import print_data
def make_list_incidents(data, name, sex, parallel, letter, causes, info_about_causes, time_causes, previous_causes):
    example_list_incidents = []
    for i in range(0, data.shape[0]):
        if causes[i] != 0:
            school_class = str(parallel[i]) + ' "' + letter[i] + '"'
            example_list_incidents.append(
                [name[i], sex[i], school_class, time_causes[i], info_about_causes[i], previous_causes[i]])
    return example_list_incidents


def intersection_of_classes(example_list_incidents, user_selection, info, func):
    count = 0
    students = []
    for i in range(len(example_list_incidents)):
        if example_list_incidents[user_selection][2] == example_list_incidents[i][2] and user_selection != i:
            if func == 0:
                count = count + 1
            elif func == 1:
                students.append(example_list_incidents[i][0])
    if func == 0:
        info.append([count, example_list_incidents[user_selection][2]])
    elif func == 1:
        return students


def intersection_of_time(example_list_incidents, user_selection, info, func):
    count = 0
    students = []
    for i in range(len(example_list_incidents)):
        if example_list_incidents[user_selection][3] == example_list_incidents[i][3] and user_selection != i:
            if func == 0:
                count = count + 1
            elif func == 1:
                students.append(example_list_incidents[i][0])
    if func == 0:
        info.append([count, example_list_incidents[user_selection][3]])
    elif func == 1:
        return students


def intersection_of_previous_causes(example_list_incidents, participants):
    maximum = [0, 0]
    for i in range(len(example_list_incidents)):
        for j in range(len(participants)):
            if example_list_incidents[i][0] == participants[j] and example_list_incidents[0][5] > int(maximum[1]):
                maximum = [example_list_incidents[i][0], example_list_incidents[i][5]]
    return maximum


def distribute_points(example_list_incidents, user_selection, info):
    is_fight = 0
    is_personal = 0
    is_class = 0
    additional_info = []
    if info[0][0] != 0 and info[1][0] != 0:
        is_fight = is_fight + 1
    return [is_fight, is_personal, is_class, additional_info]


def conclusions(example_list_incidents, user_selection, info):
    participants = None
    if info[0][1] != 0:
        participants = intersection_of_time(example_list_incidents, user_selection, info, 1)
    elif info[0][0] != 0:
        participants = intersection_of_classes(example_list_incidents, user_selection, info, 1)
    maximum = intersection_of_previous_causes(example_list_incidents, participants)
    if maximum[1] != 0:
        suspicious = 1
    else:
        suspicious = 0
    if info[0][0] != 0:
        class_matters = 1
    else:
        class_matters = 0
    if info[1][0] != 0:
        time_matters = 1
    else:
        time_matters = 0
    if time_matters == 1 and class_matters == 1:
        return print_data.is_fight(1, info[1][0], info[0][0], info[0][1], suspicious, maximum)
    elif time_matters == 1 and class_matters == 0:
        return print_data.is_fight(0, info[1][0], 0, 0, suspicious, maximum)
    elif time_matters == 0 and class_matters == 1:
        return print_data.is_incident_in_classroom(info[0][0], info[0][1], suspicious, maximum)
    else:
        return print_data.is_personal_incident()
