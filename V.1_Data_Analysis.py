import pandas as pd
import numpy as np
import math
import sys
def count(colum) -> int:
    
    index = 0
    if colum.dtype == object:
        return 
    for value in colum:
        if np.isnan(value):
          index = index + 1
    return len(colum) - index

def mean(colum) -> float:

    index = 0
    if colum.dtype == object:
        return 
    return colum.sum() / len(colum)

def std(colum)-> float:

    mean_value = mean(colum)

    va = lambda x : math.pow(x - mean_value,2)
    stander = sum(list(map(va, colum)))
   
    return math.sqrt(stander/len(colum))

def min(colum)-> float:

    min_value = sys.maxsize
    for value in colum:
        if value < min_value:
          min_value = value 
    return min_value

def max(colum)-> float:

    max_value = float('-inf')
    for value in colum:
        if value > max_value:
          max_value = value 
    return max_value

def main() -> None:
    df = pd.read_csv("dataset_test.csv")
    # print(df.dtypes)
    print(df.describe())
    print("count",count(df['Index']))
    print("mean",mean(df['Index']))
    print("std",std(df['Index']))
    print("min",min(df['Index']))
    print("max",max(df['Index']))
    
main()