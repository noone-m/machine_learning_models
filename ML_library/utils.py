import numpy as np


def mse(y,y_hat):
    """
     compute the mean squared error function

     parameters:
     y(np.array) :  target values (true value)
     y_hat(np.array) : predicted values

     returns:
     mse (float) : the mean squared error value
    """

    se = (y-y_hat)**2
    mse_ = np.sum(se) / len(y)
    return mse_




