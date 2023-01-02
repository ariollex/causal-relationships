import pandas
import numpy
import input_data
import calculations
import print_data
import charts
from strings import print_on_language, set_language

# Version
version = '0.0.2-debug-closed'

# Language
language = open("current_language", 'r').read()
set_language(language)
print(print_on_language(1, 15), version)
print('If you want to close the program, press "E"', end='\n\n')
print('Current language: ', language, '. If you want to change the language, enter L at any time.', sep='', end='\n\n')

# Dataset
file_loc = 'Dataset/Cause-effect-pairs-in-school.xlsx'
data = pandas.read_excel(file_loc)
data.columns = range(data.columns.size)
data.replace(numpy.nan, 0, inplace=True)

# Dataset settings
name = data[0]
sex = data[1]
parallel = data[2]
letter = data[3]
causes = data[4]
info_about_causes = data[5]
time_causes = data[6]

# List with output data
info = []

# Other
user_selection = -2
choice_mode = -2
graphs = [print_on_language(1, 5), print_on_language(1, 18)]

# Program operation mode selection
functions = [print_on_language(1, 8), print_on_language(1, 9)]
while choice_mode == -2 or choice_mode == -1:
    if choice_mode == -2:
        print(print_on_language(1, 6) + ':')
        for i in range(len(functions)):
            print(i + 1, ') ', functions[i], sep='')
        print(print_on_language(1, 7) + ':', end=' ')
    choice_mode = input_data.make_user_choice(functions)

# Creating a list of incidents
list_incidents = calculations.make_list_incidents(data, name, sex, parallel, letter, causes, info_about_causes,
                                                  time_causes)

if choice_mode == 0:
    # Incident selection
    while user_selection == -2 or user_selection == -1:
        if user_selection == -2:
            print_data.print_list_incidents(list_incidents)
        user_selection = input_data.make_user_choice(list_incidents)

    print(print_on_language(1, 2), ' ', user_selection + 1,
          '. ' + print_on_language(2, 2) + ': '
          if list_incidents[user_selection][1] == print_on_language(1, 4) or print_on_language(3, 2) == 0
          else '. ' + print_on_language(3, 2) + ': ', list_incidents[user_selection][0], sep='')

    # Calculations
    calculations.intersection_of_classes(list_incidents, user_selection, info)

    # Data output
    print_data.print_info(info)

elif choice_mode == 1:
    choice_graph = -1
    print(print_on_language(1, 10) + ':')
    for i in range(len(graphs)):
        print(i + 1, ') ', graphs[i], sep='')
    print(print_on_language(1, 11) + ':', end=' ')
    # Graph selection
    while choice_graph == -2 or choice_graph == -1:
        choice_graph = input_data.make_user_choice(graphs)
    if choice_graph == 0:
        charts.graph_1(data, causes, list_incidents)
    elif choice_graph == 1:
        charts.graph_2(data, list_incidents, parallel)