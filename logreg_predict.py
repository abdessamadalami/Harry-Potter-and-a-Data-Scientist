import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys,os
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


def sigmoid(z):
        z = np.clip(z, -500, 500)  # Prevent overflow
        return 1 / (1 + np.exp(-z))

def add_intercept(X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

def predict_prob(X,theta):
        # X = add_intercept(X)
        return sigmoid(np.dot(X, theta))


def logreg_predict(weights_df, data_pr ):
       
    weights_df = pd.read_csv("weights.csv", index_col=0)
    data_pr = pd.read_csv("dataset_test.csv")
    
    data_pr = data_pr[list(weights_df.columns)]
    data_pr[data_pr.select_dtypes(include=[np.number]).columns] = data_pr.select_dtypes(include=[np.number]).apply(
        lambda x: x.fillna(x.mean()), axis=0
    )

    X_scaled = scaler.fit_transform(data_pr)
    output_df = pd.DataFrame()
    for index ,wei_row in weights_df.iterrows():
        pred = predict_prob(X_scaled, wei_row)
        output_df[index] =  pred * 100
    # output_df['house'] = houses


    output_df["Hogwarts House"] = (output_df.select_dtypes('number').idxmax(axis=1))
    print(output_df.head(5))
    # output_df.insert(0, "index")
    output_df.reset_index(inplace=True)
    output_df.to_csv('./houses.csv', columns=["index", "Hogwarts House"], index=False)

def main():
        
        try:
            if len(sys.argv) != 3:
                raise AssertionError("Incorrect number of arguments")
            else:
                weights_path = sys.argv[1]
                test_path = sys.argv[2]
                if os.path.exists(weights_path) and os.path.exists(test_path):
                    weights_df = pd.read_csv("weights.csv", index_col=0)
                    data_pr = pd.read_csv("dataset_test.csv")
                    logreg_predict(weights_df=weights_df, data_pr=data_pr)
                else:
                    print("File does not exist.")
        except AssertionError as error:
            print(AssertionError.__name__ + ":", error)
    
if __name__ == "__main__":
    main()