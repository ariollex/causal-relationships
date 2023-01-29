import matplotlib.pyplot as plt
import seaborn as sns
from strings import print_on_language

list_incidents, causes, parallel, name_columns, language_texts, previous_causes = [], [], [], [], [], []


def set_variables(example_list_incidents, example_causes, example_parallel, example_name_columns,
                  example_previous_causes):
    global list_incidents, causes, parallel, name_columns, previous_causes
    name_columns = example_name_columns
    list_incidents, causes, parallel, = example_list_incidents, example_causes, example_parallel
    previous_causes = example_previous_causes


def chart_selection(choice_graph, data):
    plt.close('all')
    if choice_graph == 0:
        chart_number_of_incidents_to_students(data)
    elif choice_graph == 1:
        chart_incidents_on_parallel(data)
    elif choice_graph == 2:
        correlation_chart(data)
    elif choice_graph == 3:
        chart_boxplot(data)


def chart_boxplot(data):
    global previous_causes
    previous_causes = previous_causes  # Исправляет предупреждение
    incident_count = previous_causes.value_counts().sort_values(ascending=False).index.values
    sns.boxplot(y=previous_causes, x=parallel, data=data[previous_causes.isin(incident_count)], orient="h")
    plt.locator_params(axis='x', nbins=max(parallel) + 1)
    plt.legend([], loc='upper right', title='2 - ' + str(name_columns[2]) + '\n6 - ' + str(name_columns[6]))
    plt.show()


def chart_number_of_incidents_to_students(data):
    plt.hist(causes, bins=2, label=print_on_language(1, 12) + ' / ' + print_on_language(1, 13) + ', %: ' + str(
        round((len(list_incidents) / data.shape[0] * 100), 3)))
    plt.xlabel(print_on_language(1, 12))
    plt.ylabel(print_on_language(1, 13))
    plt.locator_params(axis='y', nbins=10)
    plt.locator_params(axis='x', nbins=2)
    plt.legend()
    plt.show()


def chart_incidents_on_parallel(data):
    causes_df = data[[4] + [2]]
    causes_df.groupby(2).sum().plot(kind='bar', rot=0)
    plt.xlabel(print_on_language(1, 17))
    plt.ylabel(print_on_language(1, 12))
    plt.locator_params(axis='y', nbins=max(causes_df) + 1)
    plt.locator_params(axis='x', nbins=max(parallel) + 1)
    plt.legend([], loc='upper right', title=print_on_language(1, 16) + ': ' + str(len(list_incidents)))
    plt.show()


def correlation_chart(data):
    sns.heatmap(data.drop([0, 1, 3], axis=1).corr(method='pearson', min_periods=1, numeric_only=False),
                linewidths=0.1, annot=True)
    plt.legend([], loc='upper right',
               title='2 - ' + str(name_columns[2]) + '\n4 - ' + str(name_columns[4]) +
                     '\n5 - ' + str(name_columns[5]) + '\n6 - ' + str(name_columns[6]))
    plt.show()
