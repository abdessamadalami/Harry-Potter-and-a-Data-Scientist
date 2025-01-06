
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=1, lambda_param=0.1, algo = "MBGD"):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = False
        self.lambda_param = lambda_param
        self.algo = algo
        self.batch_size = 32
    
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)
    
    def __sigmoid(self, z):
        z = np.clip(z, -500, 500)  # Prevent overflow
        return 1 / (1 + np.exp(-z))
    
    def __loss(self, h, y):
        epsilon = 1e-15  # for log(0)
        h = np.clip(h, epsilon, 1 - epsilon)  # Clip values to prevent log(0)
        return (-y * np.log(h) - (1 - y) * np.log(1 - h))/y.size
    
    def stochastic_gd(self,X,y):
       
        n_samples, n_features = X.shape
        self.theta = np.random.randn(n_features)
        
        for index in range(self.num_iter):
            
            indices = np.random.permutation(n_samples)
            X_shuffled = X[indices]
            y_shuffled = y[indices]
            for i in range(0, n_samples, self.batch_size):

                X_batch = X_shuffled[i:i+self.batch_size]
                y_batch = y_shuffled[i:i+self.batch_size]

                z = np.dot(X_batch, self.theta)
                h = self.__sigmoid(z)

                # loss function derivitive 
                gradient = np.dot(X_batch.T, (h - y_batch)) / y_batch.size 

                # gradient += (self.theta) / y.size
                # θ_new = θ_old - α * ∂J/∂θ
                self.theta -= self.lr * gradient
                loss = self.__loss(h, y_batch)

                if(self.num_iter % 10000 == 0):
                    print(f'Iteration {i}, Loss: {loss:.4f}')

    def mini_batch(self, X, y):
        
        n_samples, n_features = X.shape
        self.theta = np.random.randn(n_features)
        
       
        for index in range(self.num_iter):
            
            for i in range(0, n_samples, self.batch_size):
                
                X_batch = X[i:i+self.batch_size]
                y_batch = y[i:i+self.batch_size]
                
                # print("This is y ", i + self.batch_size, n_samples, len(X_batch))

                z = np.dot(X_batch, self.theta)
                h = self.__sigmoid(z)

                # loss function derivitive 
                gradient = np.dot(X_batch.T, (h - y_batch)) / y_batch.size 

                self.theta -= self.lr * gradient
                loss = self.__loss(h, y_batch)
            if(index % 10000 == 0):
                print(f'Iteration {i}, Loss: {loss:.4f}')


    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)
        
        # weights initialization
        self.theta = np.zeros(X.shape[1])

        if (self.algo == "SGD"):
            self.stochastic_gd(X=X,y=y)
            
        if (self.algo == "MBGD"):
            print("hello ")
            self.mini_batch(X=X, y=y)
        else:    
            for i in range(self.num_iter):

                z = np.dot(X, self.theta)
                h = self.__sigmoid(z)

                # loss function derivitive 
                gradient = np.dot(X.T, (h - y)) / y.size 
                print(gradient)
                self.theta -= self.lr * gradient
                # loss = self.__loss(h, y)
                # if(self.pr_loss and i % 10000 == 0):
                #     print(f'Iteration {i}, Loss: {loss:.4f}')
