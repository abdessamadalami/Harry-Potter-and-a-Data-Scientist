import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_train.csv")

std_values = df.select_dtypes(include='number').std()

std_df  = pd.DataFrame(std_values).reset_index() 
std_df.columns = ['coures', 'std_val']
min_val = std_df.std_val.min()
feather = (std_df['coures'][(std_df.std_val == min_val)].values[0])
print("this is the feather ==> ", feather)
sns.histplot(df, x=feather, hue="Hogwarts House", element="step")