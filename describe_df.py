from pandas.api.types import is_numeric_dtype
import pandas as pd
import numpy as np
import math
import sys

class describ:

    def __init__(self, df):

        # self.count
        # self.mean
        # self.std
        # self.min
        # self.max
        # self.q1
        # self.q2
        # self.q3
        self.des_col = []
        self.des_set = []
        print("constrctor ")
        for colum in df:
            if is_numeric_dtype(df[colum]):
                # print (self.count(df[colum]))
                # print (self.mean(df[colum]), df[colum].mean())
                print (self.std(df[colum]), df[colum].std())
                # self.max(colum)
                # self.min(colum)
                # self.percentile(colum)

    def count(self, colum) -> int:
        index = 0
        if colum.dtype == object:
            return 
        for value in colum:
            if np.isnan(value):
             index = index + 1
        return len(colum) - index

    def mean(self,colum) -> float:

        index = 0
        colum = colum.dropna()
        if colum.dtype == object:
            return 
        return colum.sum() / len(colum)

    def std(self, colum)-> float:
        print("dro",len(colum.dropna()))
        mean_value = self.mean(colum)
        print("len",len(colum))
        colum = colum.dropna()
        print(("dro", len(colum)))
        va = lambda x : math.pow(abs(x - mean_value),2)
        stander = sum(list(map(va, colum)))
        print("stander ", stander,  len(colum))
        std = math.sqrt(stander/k)
        return std

    def min(self, colum)-> float:

        min_value = sys.maxsize
        for value in colum:
            if value < min_value:
              min_value = value 
        return min_value

    def max(self, colum)-> float:

        max_value = float('-inf')
        for value in colum:
            if value > max_value:
             max_value = value 
        return max_value

    def percentile (self, value):
        qan_list = sorted(value.dorpna())
        self.q1 = (25/100) * (len(value) + 1)
        self.q2 = (50/100) * (len(value) + 1)
        self.q3 = (75/100) * (len(value) + 1)

