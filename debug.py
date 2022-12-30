import matplotlib.pyplot as plt
import numpy
import pandas
import main

def debuglist(list):
    for i in range(len(list)):
        print(list[i])


def debugdataset(dataset):
    print(dataset.head)
    print(dataset.shape)

plt.style.use('fivethirtyeight')
plt.hist(main.formatcauses, bins = 100, edgecolor = 'k')
plt.xlabel('Causes'); plt.ylabel('Student')
plt.show()