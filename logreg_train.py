import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import pandas as pd
from LogisticRegression import LogisticRegression
import sys
import os

# print(df.describe()['mean'])
# print(df.dtypes)
house_i = {'Slytherin' : 1, 
         'Gryffindor': 2,
         'Hufflepuff': 3,
         "Ravenclaw" : 4}

#  display(df.head(10))
def sigmoid(z):
    # Compute the sigmoid function using the formula: 1 / (1 + e^(-z)).
    sigmoid_result = 1 / (1 + np.exp(-z))
    
    # Return the computed sigmoid value.
    return sigmoid_result

def scal_df(X):
    X_scaled = np.empty((0,0),float)

    for colum in X:
        np_ser = []
        mean_df = X[colum].mean()
        std_df = X[colum].std()
        
        for elem in X[colum]:
            elem = (elem -mean_df)/std_df
            np_ser.append(elem)
        
        column = np.array(np_ser).reshape(-1, 1)  # Convert the list to a column
        if X_scaled.size == 0:  # If the array is empty, initialize it
            X_scaled = column
        else:
            X_scaled = np.hstack((X_scaled, column))  # Horizontally stack the new column
    return X_scaled

def heatmap(trian_df):
    core_matrix = trian_df.select_dtypes('number').corr()
    plt.figure(figsize=(20,10))
    sns.heatmap(core_matrix, annot=True)

def strong_correlations(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr

def pre_prossceing(df):
    df[df.select_dtypes(include=[np.number]).columns] = df.select_dtypes(include=[np.number]).apply(
        lambda x: x.fillna(x.mean()), axis=0
    )
    ineffectual_colums = strong_correlations(df.select_dtypes('number'), 0.6)
    # print(ineffectual_colums)
    trian_df = df.drop(columns=ineffectual_colums)
    return trian_df


# mapping house index 
def logreg_train(df):
    
    df = pd.read_csv("dataset_train.csv")
    trian_df = pre_prossceing(df)
    trust_house = trian_df['Hogwarts House'].map(house_i)
    trian_df = trian_df.select_dtypes('number')

    X_scaled = scal_df(trian_df)

    X_weights = np.empty((0,0),float)
    houses = []
    i = 1
    while i <= 4:
        y = (trust_house == i) * 1 # we preduct just for one now 
        
        y = y.to_numpy()
        # print(i)
        model_custom = LogisticRegression(lr=0.01, num_iter=1000, lambda_param=1.0, algo="MBGD")
        model_custom.fit(X_scaled, y)
        
        key = [k for k, v in house_i.items() if v == i]
        houses.append(key[0])
        column = np.array(model_custom.theta).reshape(-1, 1)  # Convert the list to a column
        if X_weights.size == 0:  # If the array is empty, initialize it
            X_weights = column
        else:
            X_weights = np.hstack((X_weights, column))  # Horizontally stack the new column
        i+=1
        
        

    # df = pd.DataFrame(X_weights.T, index=houses)
    df = pd.DataFrame(X_weights.T,columns=trian_df.columns ,index=houses)
    df.to_csv("weights.csv")

def main():
        try:
            if len(sys.argv) != 2:
                raise AssertionError("Incorrect number of arguments")
            else:
                file_path = sys.argv[1]
                if os.path.exists(file_path):
                        df = pd.read_csv(file_path)
                        logreg_train(df)
                else:
                    print("File does not exist.")
        except AssertionError as error:
            print(AssertionError.__name__ + ":", error)
    
if __name__ == "__main__":
    main()
