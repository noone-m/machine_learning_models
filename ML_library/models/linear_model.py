import numpy as np
from utils import mse

class LinearRegression:
    """ represent linear regression model"""
    def train(self,X,y):
        y = y.reshape((y.shape[0],1))
        n = X.shape[1]
        W_init = np.zeros((n,1))
        W = gradient_decent(X,y,)
        y_hat = np.matmul(X,W)
        mean_error = mse(y,y_hat)
