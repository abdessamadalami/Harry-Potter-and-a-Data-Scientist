
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=1, lambda_param=0.1):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = False
        self.lambda_param = lambda_param
    
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)
    
    def __sigmoid(self, z):
        z = np.clip(z, -500, 500)  # Prevent overflow
        return 1 / (1 + np.exp(-z))
    
    def __loss(self, h, y):
        epsilon = 1e-15  # for log(0)
        h = np.clip(h, epsilon, 1 - epsilon)  # Clip values to prevent log(0)
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    
    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)
        
        # weights initialization
        self.theta = np.zeros(X.shape[1])
        
        # To store loss history
        self.loss_history = []
        
        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)

            # loss function derivitive 
            gradient = np.dot(X.T, (h - y)) / y.size 
            
            # gradient += (self.theta) / y.size
            # θ_new = θ_old - α * ∂J/∂θ
            self.theta -= self.lr * gradient
            loss = self.__loss(h, y)
            
            if(self.pr_loss and i % 10000 == 0):
                print(f'Iteration {i}, Loss: {loss:.4f}')
