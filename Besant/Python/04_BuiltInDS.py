'''
Ref:
https://docs.python.org/3/tutorial/datastructures.html

# what is a bult-in-data structures?


# why we need them ?


# how to use them ?


# Is there an alterante to it?
collections, numpyarray, dataframe in pandas
'''

# built -in types
# List, tuple, set, dict 
'''
# syntax:
# <var name> = [value1, value2, value3,...]
foo = [100, "hello", True, None]
print(foo)
x=foo[0]
y = foo[3]

# add entries to list
foo.append(200)
print("foo after append", foo)
foo.insert(2, 300)
print("Foo after insert", foo)
# delete entries from list
foo.pop()
foo.remove(2)
foo.reverse

# tuple 
# read only lists 
mytuple = (100, "Hello", True, None)
mytuple[1]


# List -> is an array usually contains 100, 70, 85

mixedList = [50, 10, 40]
clone = mixedList.copy()
print("At Start mixedList", mixedList)
print("At Start clone", clone)
mixedList.insert(1, 20)
clone.append(10)
print("At the end mixedList", mixedList)
print("At the end clone ", clone)


myTuple = ("100", 10 , True)
myTuple[0]
myTuple[1]


len(mixedList)

print("List at the start", mixedList)
mixedList.pop()
print("After pop", mixedList)
mixedList.remove("100")
print("After remove", mixedList)



myList = [100, 70, 85]
print("before rev:", myList)
myList.reverse()
print("After rev:", myList)

# push & pop -> push: append or insert ; pop -> remove, delete; Stack is LIFO hence push and pop and the end or rear


# queue: enqueue, deque; enqueue: append, insert at the rear ; deque; remove from the front
# myList.pop(0)

# Tuple
# List vs Tuple
 

myList = list([100, 70, 85])
# above is eq to myList = [100, 70, 85]
print(myList)
course = "bachelors", "masters", "dipolma" 
# const, read-only , immutable





basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

#hash map or map

from pickle import NONE
from xmlrpc.client import Boolean


studentRec = { 100: "foo", 101:"foo", 102: "bar"}
print(studentRec)    
print(type(studentRec.keys()))
print(studentRec.get(102))

isStudentFound = False;
if studentRec.get(102) != NONE & studentRec.get(101) != NONE:
    isStudentFound = True
    
print(isStudentFound)


# Stack-> LIFO 
# queue -> FIFO




rainbow = {"violet", "indigo", "blue", "green", "yellow", "orange", "red"}
iscolourRedFoundInRainbow = "red" in rainbow
print(iscolourRedFoundInRainbow)
isWhiteInRainbow = "white" in rainbow
print(isWhiteInRainbow)
'''


myList = [100, 200, 200, 300, 400]
print(myList[2:4])