import pandas
import numpy
from tkinter import *
import os

import error
import calculations
import print_data
import graphs
from strings import print_on_language, set_language, set_variables

# Disable warnings
pandas.options.mode.chained_assignment = None

# Configuration
configuration = open("configuration", 'r').read().split('\n')
calculations.set_variables(configuration)
indexes, warnings, missing_parameters = calculations.check_configuration()
if len(warnings) != 0:
    [error.warning(warnings[i]) for i in range(len(warnings))]
if len(missing_parameters) != 0:
    error.error('These required parameters are not defined:', 0)
    print(*['- ' + missing_parameters[i] for i in range(len(missing_parameters))], sep='\n')
    error.broken_configuration()
set_variables(configuration, indexes)
errors = calculations.check_parameters()
if len(errors) != 0:
    error.error('Incorrect parameter values:', 0)
    print(*['- ' + errors[i] for i in range(len(errors))], sep='\n')
    error.broken_configuration()

# Version
version = calculations.read_from_configuration(0)
prefix = calculations.read_from_configuration(1)
version = 'v' + version + '-' + prefix

# Language
language = calculations.read_from_configuration(2)
delayed_start = []
if not set_language(language):
    delayed_start.append('language')

# Dataset
file_loc = calculations.read_from_configuration(10)
data = pandas.read_excel(file_loc)
name_columns = list(data)
data.columns = range(data.columns.size)
data.replace(numpy.nan, 0, inplace=True)

# Dataset settings
name = data[int(calculations.read_from_configuration(3)) - 1]
sex = data[int(calculations.read_from_configuration(4)) - 1]
parallel = data[int(calculations.read_from_configuration(5)) - 1]
letter = data[int(calculations.read_from_configuration(6)) - 1]
causes = data[int(calculations.read_from_configuration(7)) - 1]
time_causes = data[int(calculations.read_from_configuration(8)) - 1]
previous_causes = data[int(calculations.read_from_configuration(9)) - 1]

# Convert time
for i in range(data.shape[0]):
    time_causes[i] = int(str(time_causes[i]).replace(':', '')) if time_causes[i] != 0 else int(time_causes[i])


def change_language():
    files = os.listdir('languages')
    clear_window()
    Label(window, text='Available languages:').grid(column=0, row=0)
    count_row = 1
    for i in range(len(files)):
        Button(window, text=files[i].replace('strings_', '').replace('.xlsx', ''),
               command=lambda j=i: change_language_process(files, j)).grid(column=0, row=count_row)
        count_row = count_row + 1
    Label(window, text='Please note that if the dataset and the program language are different, there may be errors.') \
        .grid(column=0, row=count_row + 1)


def clear_window(message=None):
    for widget in window.winfo_children():
        widget.destroy()
    if message is not None:
        Label(window, text=message).grid(column=0, row=0)


def change_language_process(files, index_language):
    new_language = files[index_language].replace('strings_', '').replace('.xlsx', '')
    set_language(new_language)
    exit_screen(print_on_language(1, 14))


def exit_screen(message=None):
    if message is not None:
        clear_window(message)
    Button(window, text=print_on_language(1, 21), command=exit).grid(column=0, row=1)


def mode_selection(clear=False):
    if clear:
        clear_window()
    Label(window, text=print_on_language(1, 6) + '. ' + print_on_language(1, 7) + ':').grid(column=0, row=0)

    # Program operation mode selection
    Button(window, text=modes[0], command=mode_causal_relationship).grid(column=0, row=1)
    Button(window, text=modes[1], command=mode_graph).grid(column=0, row=2)
    Button(window, text=print_on_language(1, 20), command=change_language).grid(column=0, row=3)
    Button(window, text=print_on_language(1, 21), command=exit).grid(column=0, row=4)


def mode_causal_relationship():
    clear_window()
    info = []
    list_incidents_numbered = print_data.print_list_incidents(list_incidents)
    Label(window, text=print_on_language(1, 0)).grid(column=0, row=0)
    count_row = len(list_incidents_numbered)
    for i in range(count_row):
        Button(window, text=list_incidents_numbered[i], command=lambda j=i: mode_causal_relationship_process(j, info)) \
            .grid(column=0, row=i + 1)
    Button(window, text='Back', command=lambda: mode_selection(clear=True)).grid(column=0, row=count_row + 1)
    Button(window, text=print_on_language(1, 21), command=exit).grid(column=1, row=count_row + 1)


def mode_causal_relationship_process(user_selection, info):
    clear_window()
    if list_incidents[user_selection][1] == print_on_language(1, 4) or (print_on_language(3, 2) == 0):
        user_choice_text = print_on_language(1, 2) + ' ' + str(user_selection + 1) + '. ' + print_on_language(2, 2) + \
                           ': ' + list_incidents[user_selection][0]
    else:
        user_choice_text = print_on_language(1, 2) + ' ' + str(user_selection + 1) + '. ' + print_on_language(3, 2) + \
                           ': ' + list_incidents[user_selection][0]
    Label(window, text=user_choice_text).grid(column=0, row=0)

    # Calculations: search for matching information
    calculations.intersection_of_classes(list_incidents, user_selection, info, 0)
    calculations.intersection_of_time(list_incidents, user_selection, info, 0)

    # Calculations: conclusions
    Label(window, text=calculations.conclusions(list_incidents, user_selection, info)).grid(column=0, row=1)
    Button(window, text='Back', command=lambda: mode_selection(clear=True)).grid(column=0, row=2)
    Button(window, text=print_on_language(1, 21), command=exit).grid(column=1, row=2)


def mode_graph():
    clear_window()
    list_graphs_numbered = print_data.print_selection_list(available_graphs)
    Label(window, text=print_on_language(1, 10) + ':')
    count_row = len(list_graphs_numbered)
    for i in range(count_row):
        Button(window, text=list_graphs_numbered[i], command=lambda j=i: mode_graph_process(j)).grid(column=0, row=i + 1)
    Button(window, text='Back', command=lambda: mode_selection(clear=True)).grid(column=0, row=count_row + 1)
    Button(window, text=print_on_language(1, 21), command=exit).grid(column=1, row=count_row + 1)


def mode_graph_process(choice_graph):
    graphs.set_variables(list_incidents, causes, parallel, name_columns)
    graphs.graph_selection(choice_graph, data)
    count_row = len(available_graphs)
    Button(window, text='Back', command=lambda: mode_selection(clear=True)).grid(column=0, row=count_row + 1)
    Button(window, text=print_on_language(1, 21), command=exit).grid(column=1, row=count_row + 1)


root = Tk()
window = Frame()
window.pack(fill="both", expand=True)

if len(delayed_start) != 0:
    root.title('Causal relationships in school ' + version)
    for i in range(len(delayed_start)):
        if i == len(delayed_start):
            break
        if delayed_start[i] == 'language':
            change_language()
            delayed_start.remove('language')
else:
    # Modes
    modes = [print_on_language(1, 8), print_on_language(1, 9)]

    # Available graphs
    available_graphs = [print_on_language(1, 5), print_on_language(1, 18), print_on_language(1, 19)]

    # Creating a list of incidents
    list_incidents = calculations.make_list_incidents(data, name, sex, parallel, letter, causes,
                                                      time_causes, previous_causes)

    root.title(print_on_language(1, 15) + ' ' + version)
    mode_selection()
root.mainloop()
