
'''
# what is a lambda function?
Syntatic sugar to regular function

How to use them?
Syntax:
    <variable name> = lambda (argument1, argument2, ...) ()
'''

# Function to sqaure two numbers
def square(nums):
    mySquare = []
    for i in nums:
        mySquare.append(i*i)
    return mySquare


# Lamda function

mySquare = lambda myList : myList*myList
print("Sqaure using lambda function", mySquare([1, 2, 3, 4, 5]))


# Topic: Higher order functions -> nothing but function which takes another function as input arg
# e.g map, filter, reduce

# syntax:
# map(function_to_apply, list_of_inputs)
from functools import map
from functools import reduce

nums = [1, 2, 3, 4, 5]

# Finding sqaures of all nums in a list
def square(nums):
    mySquare = []
    for i in nums:
        mySquare.append(i*i)
    return mySquare

# Finding sqaures of all nums in a list using 'map'
squared = list(map(lambda x: x**2, nums))

nums = range(-5, 5)
gtThanZero = list(filter(lambda x: x > 0, nums))
print(gtThanZero)


# To get products of all elements in a  list
nums = [1, 2, 3, 4]
product = 1
for num in nums:
    product = product * num

# To get products of all elements in a list using "reduce"
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


'''
Things to try:
    1. Write a lambda function to add two numbers
    2. Given a list of numbers sort them by their frequency
        e.g: [10, 2, 5, 2, 5 , 5 , 10] , result = [2, 10, 5]
'''
   