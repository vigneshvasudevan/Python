'''
Ref:
https://docs.python.org/3/tutorial/datastructures.html

# what is a bult-in-data structures?
List, tuple, sets, dictionaries

# why we need them ?
Store data as per the needs say faster retrievel

# Is there an alterante to it?
collections, numpyarray, dataframe in pandas
'''



'''
-------------------------
Topic: List
-------------------------
Syntax:
<var name> = [value1, value2, value1,...]
Here 
1. value1 and value2 may or may not be of same datatype.
2. Duplicates are allowed in list

List is zero based index, in other words first element of the 
list has index '0'
'''

foo = [100, "hello", True, None]
print(foo)
print("First element of list 'Foo' is = ",foo[0])
print("4th element of list 'Foo' is = ",foo[3])

# add entries to list
foo.append(200)
print("foo after append", foo)
foo.insert(2, 300)
print("Foo after insert", foo)
# delete entries from list
foo.pop()
foo.remove(2)
foo.reverse

print("Get elements until 2nd index", foo[:2])
print("Get elements starting from 1st index untill end", foo[1:])
print("Get elements starting from 1st index untill 3rd", foo[1:3])



'''
----------------------------
Topic: Shallow copy in list
----------------------------
'''
mixedList = [50, 10, 40]
clone = mixedList.copy()
print("At Start mixedList", mixedList)
print("At Start clone", clone)
mixedList.insert(1, 20)
clone.append(10)
print("At the end mixedList", mixedList)
print("At the end clone ", clone)




'''
-------------------------
Topic: Tuple
-------------------------
Syntax:
<var name> = (value1, value2, value3,...)

Tuples are same as list but they are read-only aka const, immutable
''' 
mytuple = (100, "Hello", True, None)
print("2nd element in myTuple =",mytuple[1])



'''
-------------------------
Topic: List vs Tuple
-------------------------
When to choose List and Tuple
'''

# Some examples when tuple is preferred over list
# 
# 1. College offering only limited courses
# 2. Student names of a class where students can't enroll in
# the middle of the course and student can't drop out.
course = ("bachelors", "masters", "diploma" )





'''
--------------------------------------------------------
Topic: Sets
Syntax:
<var name> = {value1, value2, value3,...}

here
1. Every value in the set must be unique
2. value1 & value2 may or may not be of same primitive type
-----------------------------------------------------------
'''

rainbow = {"violet", "indigo", "blue", "green", "yellow", "orange", "red"}
print("Rainbow has 7 unique colors and they are =", rainbow)
print("Is red found in rainbow", "red" in rainbow)
print("Is grey found in rainbow", "grey" in rainbow)


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket ignoring duplicates ", basket)
basket.add("jackfruit")
print("basket after adding one fruit", basket)





'''
--------------------------------------------------------
Topic: Dictionaries
Syntax:
<var name> = {key1 : value1, key2: value2, key3: value1,...}

here
1. Every key in the set must be unique but values need not be

Dictionaries as same as hashmap or map in other programming
languages
-----------------------------------------------------------
'''
studentRec = { 100: "foo", 101:"foo", 102: "bar"}
print(studentRec)    
print(type(studentRec.keys()))
print("Accessing dict value using get operator", studentRec.get(102))
print("Accessing dict value using [] operator",studentRec[100])
print("Accessing invalid key", studentRec[104])


'''
Things to try:
    1. Implement stack and queue using List
    2. To create a empty set and later add entries
        Hint: use mySet = set() instead of mySet = {}
'''