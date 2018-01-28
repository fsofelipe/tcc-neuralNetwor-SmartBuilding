from sklearn import preprocessing
from dataNumpy import *
import numpy as np
from selector import *

Y = np.loadtxt("../Data/dataset_input.csv", delimiter=",")

print (Y[0,:])


print(Y[0, 6])
Y = np.delete(Y, 6, 1)
print(Y[0, 6])

np.savetxt("../Data/dataset_input_18.csv", Y, delimiter=',')
