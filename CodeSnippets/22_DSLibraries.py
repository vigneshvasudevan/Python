# numpy, pandas, scikit, matplotlib

# how different is numpy from List ?
#   1. numpy arrays are extremly performant
#   2. list the entries are not necessarily stored in contiguous blocks in memory
#       whereas numpy gaurantees thats. 

# 0xAAAA starting array, 100 data starting from prev address, 


# create a numpy array
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

myarray = np.array([1, 2, 3, 4, 5])
zeroArray = np.zeros(5, dtype=int)
input1 = np.linspace(5, 10, 20, dtype=int)
input2 = np.linspace(5, 10, 20)
print(input1)
print(input2)
#print(type(myarray))
#print(myarray)
#print(zeroArray)




my2dArray = np.array([[1, 2, 3, 4, 5], [10, 11, 12, 13, 14]])
#print(my2dArray)

#print(np.arange(10, dtype= int))



mySeries = pd.Series([1, 2, 3, 4])

mySeries.tail()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])


plt.bar(x, y)
plt.show()

import numpy as np
from numpy.random import default_rng

'''
x = np.linspace(0, 2, 5)
#print(x)
print(np.vander(x, 3))

# default_rng(42).random((2,3))
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2].copy()
b += 1
print("b= ", b)
print("a= ", a)

A = np.ones((2, 2))
B = np.eye(2, 2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))
print(np.block([[A, B], [C, D]]))
'''

import pandas as pd

df2 = pd.DataFrame({"A": 1.0, "B": pd.Timestamp("20130102"),"C": pd.Series(1, index=list(range(4)), dtype="float32"),"D": np.array([3] * 4, dtype="int32"),"E": pd.Categorical(["test", "train", "test", "train"]), "F": "foo"})

# exercise to understand np.block() ??
# how to plot two graphs on the same plot

# x1, y1 and x2 & y2 -> plot x1vs y1 and x2 vs y2


'''
Ref:
    https://medium.com/personal-project/numpy-pandas-and-scikit-learn-explained-e7336baecedc
    https://appdividend.com/2020/05/05/how-to-check-numpy-version-on-mac-linux-and-windows/
    https://towardsdatascience.com/top-5-machine-learning-libraries-in-python-e36e3e0e02af
    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    
    https://numpy.org/doc/stable/user/basics.html
    https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html
    https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
    https://scikit-learn.org/stable/modules/ensemble.html
'''

