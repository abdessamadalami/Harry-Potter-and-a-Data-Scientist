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
                # print ("stander ",df[colum].std(), " May ",self.std(df[colum]))
                
                # print('max===> ',df[colum].max(), self.max(df[colum]))
                # print('min===> ',df[colum].min(), self.min(df[colum]))
                print("our",self.percentile(df[colum]), "they",df[colum].quantile(0.25))
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
        mean_value = self.mean(colum)
        colum = colum.dropna()
        va = lambda x : math.pow(abs(x - mean_value),2)
        stander = sum(list(map(va , colum)))
        l = len(colum)
        if l == 0:
           return 0
        std = math.sqrt(stander/(l - 1))
        return std

    def min(self, colum)-> float:

        min_value = sys.maxsize
        for value in colum:
            if value < min_value:
              min_value = value
        if min_value == sys.maxsize:
           return 'nan'
        return min_value

    def max(self, colum)-> float:

        max_value = float('-inf')
        for value in colum:
            if value > max_value:
             max_value = value 
        if max_value == float('-inf'):
           return 'nan'
        return max_value

    def percentile (self, colum):
        colum = colum.dropna()
        if len(colum) == 0:
            return 
        qan_list = sorted(colum)
        p1 = (0.25) * (len(qan_list))+1
        frac, whole = math.modf(p1)
        if frac:
        #    Lower Value+(Decimal Part of P)×(Upper Value−Lower Value)
            l, u = int(p1) , int(p1)+1
            # print(" This p",p1,"l", l,"u", u, len(colum), frac,colum[l] +  frac * (colum[u] - colum[l]))
            p = qan_list[l] + frac * (qan_list[u] - qan_list[l])
            # print(p)
            return p
        else :
            print("ppppppppppppppppp ", (qan_list[int(p1)]), p1)
            return qan_list[int(p1)]
        # p2 = (50/100) * (len(qan_list) + 1)
        # p3 = (75/100) * (len(qan_list) + 1)

