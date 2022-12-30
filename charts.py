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
