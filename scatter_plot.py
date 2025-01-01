import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def scatter_plot(df):

    
    core_matrix = df.select_dtypes('number').corr()
    # display(core_matrix)

    j = 0
    row = ''
    col = ''
    max_correlation = 0
    while (j < 13):
        for i , elem in enumerate(core_matrix):
            if(core_matrix[elem].index[j] == elem):
                continue
            if(abs(max_correlation) <= abs(core_matrix[elem][j])):
                # print("this is element: " ,core_matrix[elem][j], " in this ",core_matrix[elem].index[j], elem)
                max_correlation = core_matrix[elem][j]
                row = elem
                col = core_matrix[elem].index[j]
            # print(core_matrix[elem].index[j], elem)
        j = j + 1
    # print ("")

    print(max_correlation, (row, col))
    sns.scatterplot(data=df, x="Astronomy", y="Defense Against the Dark Arts", hue="Hogwarts House", style="Hogwarts House")
    plt.show()


df = pd.read_csv("dataset_train.csv")
scatter_plot(df)