# Numpy, Pandas, scikit, matplotlib

# How different is numpy from List ?
#   1. numpy arrays are extremly performant
#   2. list the entries are not necessarily stored in contiguous blocks in memory
#       whereas numpy gaurantees thats. 

# 0xAAAA starting array, 100 data starting from prev address, 

import numpy as np
# Create a numpy 1-dimensional array from python List
x = np.array([1, 2, 3, 4, 5])
# Create a numpy 2-dimensional array(here 2x2 matrix) from python List
y = np.array([1, 2], [3, 4])

# Create numpy array 
a = np.array([127, 128, 129], dtype=np.int8)
print(a)
# Output : array([ 127, -128, -127], dtype=int8)
# Here An 8-bit signed integer represents integers from -128 to 127.
# Assigning the int8 array to integers outside of this range results in overflow


# Intrinsic numpy array creation
a = np.arange(10)
print(a)
# Output : array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Here arrays starting from 1 until 10  is created. 10 is exclusive here.

a = np.linspace(1., 4., 6)
# Output : array([ 1. ,  1.6,  2.2,  2.8,  3.4,  4. ])
# Here beginning = 1 end = 4, 6 values is generated such that values are linearly spaced
# where stepsize = (end - begin)/(count-1); In this example begin = 1, end = 4 , count = 6


#Identity matrix
identityMatrix = np.eye(3)
print(identityMatrix)
# Output:
# array([[1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.]])

x = np.diag([1, 2, 3])
print(x)
# Output:
# array([[1, 0, 0],
#       [0, 2, 0],
#       [0, 0, 3]])

x = np.vander(np.linspace(0, 2, 5), 2)
print(x)
# Output:
# array([[0. , 1. ],
#      [0.5, 1. ],
#      [1. , 1. ],
#      [1.5, 1. ],
#      [2. , 1. ]])


zeroArray = np.zeros(2, dtype=int)
print(zeroArray)
# Output:
# array([[0, 0],
#       [0, 0]])

matrix = np.zeros((2, 3))
print(matrix)
# Output:
# array([[0., 0., 0.],
#       [0., 0., 0.]])

from numpy.random import default_rng
default_rng(42).random((2,3))
# Output:
# array([[0.77395605, 0.43887844, 0.85859792],
#       [0.69736803, 0.09417735, 0.97562235]])


# Shallow copy inside numpy array
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]
b += 1
print('a =', a, '; b =', b)
# Output: a = [2 3 3 4 5 6] ; b = [2 3]
# Here both 'a' and 'b' points to the same memory

# Deep copy inside numpy array
a = np.array([1, 2, 3, 4])
b = a[:2].copy()
b += 1
print('a = ', a, 'b = ', b)
# Output: a =  [1 2 3 4] b =  [2 3]
# Here 'a' and 'b' operate on their own array, nothing shared


# Loading csv file into numpy array
x = np.loadtxt('simple.csv', delimiter = ',', skiprows = 1) 
print(x)
# Output :
# array([[0., 0.],
#       [1., 1.],
#       [2., 4.],
#       [3., 9.]])




import pandas as pd
# Creating Pandas series from python List
mySeries = pd.Series([1, 2, 3, 4])
mySeries.tail() #By default prints last 5 values
# Output : 
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

array = np.array([1, 2, 3, 4])
# converting the NumPy array to a Pandas series
series = pd.Series(array) 

# Creating a dataframe with different values
df = pd.DataFrame({"A": 1.0, "B": pd.Timestamp("20130102"),"C": pd.Series(1, index=list(range(4)), dtype="float32"),"D": np.array([3] * 4, dtype="int32"),"E": pd.Categorical(["test", "train", "test", "train"]), "F": "foo"})

# Reading csv file and converting into data-frame
data = pd.read_csv("logs/mock.csv")

# Getting subset of data
emp = data["emp_name", "dept"]
birthMonth = data["birth_month"]
print(type(birthMonth))
# Output : pandas.core.series.Series

# Get only IT dept employee record
ITDeptEmployeeRecord = data[data["dept"] == "IT"]

# To get statstics 
data.describe()

'''
Pandas vs numpy

Data objects: 
    Numpy: 
        1. The main data object in NumPy is an array, more particularly ndarray. 
        2. It is basically an N-dimensional array that supports a wide variety of calculations and computations. 
        3. These ndarrays are much faster than the python list based arrays as they do not involve any kind of looping. 
    
    Pandas: 
        1. The main data object in Pandas is a series. 
        2. A series is basically a one-dimensional indexed array. 
        3. By combining series objects, you can build another popular data object in pandas called DataFrames. 
        4. DataFrames are n-dimensional indexed arrays. Very close to ndarrays in numpy but indexed.
        
Type of data supported in NumPy and Pandas: 

        1. NumPy library mainly used for performing numerical computations and computations. 
        2. We can perform complex calculations on arrays fastly and easily with a range of functions provided in this module. 
        3. Whereas pandas library is primarily used for data analysis, by allowing us to work with CSV, Excel, SQL etc. It even has some inbuilt functions for data plotting and visualization.
        
        
Usage in deep learning and machine learning: 
        1. NumPy is one of the basic modules on top of which most of the other python modules are built. 
        2. The most popular machine learning tool scikit learn’s modules can be fed (accept input as) with numpy arrays only. 
        3. Same is the case with complex deep learning tools such as tensorflow. It also accepts numpy arrays as input and gives arrays as output. 
        4. Pandas data objects cannot be directly used as input for machine learning and deep learning tools. 
        5. We have to run them through several steps of preprocessing before feeding them to a machine learning module.
        
        
Performance with complex operations: 
        1. NumPy performs best when it comes to complex mathematical calculations on multidimensional arrays. 
        2. It is insanely faster than pandas when it comes to calculations such as solving linear algebra, finding gradient descent, matrix multiplications and vectorization of data etc. 
        3. It is really tedious and tough to perform these calculations on data frames and series objects in pandas. However, one should note that numpy performs best with 50,000 or less number of rows in the dataset, while pandas perform best with 500,000 rows or more when it comes to data manipulation.


Indexing in Pandas and NumPy: 
        1. The data rows are not indexed by default in numpy arrays. 
        2. However, this is not the case with pandas. 
        3. The data rows are indexed or labelled by default. 
        4. You can play with the indexes and manipulate it. You can use a column as index or change the name of labels etc. in the indexes. This is quite not possible in NumPy
'''

import matplotlib.pyplot as plt
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.show()





'''
Things to try:
    1. How to plot a line graph using 'orange' color
    2. How to plot two graphs on the same plot
    3. How to use subplots to plot more than one plot on the same window
'''

'''
Future read:
    Understand when to use what type of graph

'''


'''
Ref:
     https://numpy.org/doc/stable/user/basics.html
    https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html
    https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
    https://scikit-learn.org/stable/modules/ensemble.html
    
    https://medium.com/personal-project/numpy-pandas-and-scikit-learn-explained-e7336baecedc
    https://appdividend.com/2020/05/05/how-to-check-numpy-version-on-mac-linux-and-windows/
    https://towardsdatascience.com/top-5-machine-learning-libraries-in-python-e36e3e0e02af
    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    
   
'''

