'''

# what is a Variable?
variable is used for holding some data which is used more than once

# why we need them ?
When a data is used more than once

# how to use them ?
Syntax: <vairablename> = <value>

# Is there an alterante to it?
NA

'''




'''
----------------------
Topic: variable
----------------------
'''

x = "foo"




'''
----------------------
Topic: Primitive types
----------------------
Python supports 5 primitive types namely
    1. Integer
    2. Float -> 
    3. String(one or more characters)
    4. Boolean -> True, False
    5. None -> means nothing
    
Note: Character is a string in python whose length is 1.
'''

a = 100
print(type(a))
b = "foo"
print(type(b))
c = 100.0
print(type(c))
d = True
print(type(d))
e= 'c'
print(type(e))
f = None
print(type(f))


'''
--------------------
Topic: Duck typing
--------------------
In below example, 'x' is initially a string and it later became integer
when integer is assigned. Unlike other programming language, python is 
dynamically typed, in other words a variable can hold any value type
'''
x = "foo"
print(type(x))
x = 100
print(type(x)) 



