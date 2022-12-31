import matplotlib.pyplot as plt
from print_data import printlanguage


def graph_1(data, causes, formatcauses):
    plt.hist(causes, bins=2, label=printlanguage(1, 12) + ' / ' + printlanguage(1, 13) + ', %: ' + str(
        round((len(formatcauses) / data.shape[0] * 100), 3)))
    plt.xlabel(printlanguage(1, 12))
    plt.ylabel(printlanguage(1, 13))
    plt.locator_params(axis='y', nbins=10)
    plt.locator_params(axis='x', nbins=2)
    plt.legend()
    plt.show()


def graph_2(data, formatcauses, parallel):
    causes_df = data[[4] + [2]]
    causes_df.groupby(2).sum().plot(kind='bar', rot=0)
    plt.xlabel(printlanguage(1, 17))
    plt.ylabel(printlanguage(1, 12))
    plt.locator_params(axis='y', nbins=max(causes_df) + 1)
    plt.locator_params(axis='x', nbins=max(parallel) + 1)
    plt.legend([], loc='upper right', title=printlanguage(1, 16) + ': ' + str(len(formatcauses)))
    plt.show()