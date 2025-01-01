import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def scatter_plot(df):
    
    sns.pairplot(df, hue="Hogwarts House")
    plt.show()


df = pd.read_csv("dataset_train.csv")
scatter_plot(df)