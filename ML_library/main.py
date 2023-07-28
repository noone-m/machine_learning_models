from utils import mse
import numpy as np


y = np.array([[1],[4],[8],[16]])
y_hat = np.array([[0],[2],[7],[14]])
me = mse(y,y_hat)
print(me)