
'''
# what is a closure?
Closure enable creating wrapper function and private functions in python
'''

# closures
def foo():
    a = 100
    def bar():
        print("Value of a = ", a)
    bar()
    
foo()


'''
what is namespace?
Name = identifier or variable
Namespace is a collection of name

Python has 3 types of namespace;
    1. Built-in
    2. module global namespace
    3. Function local namespace
'''

a = 100
print('id(100) =', id(100))
print('id(a) =', id(100))
# above two outputs the same since 100 is stored at some address in memory and 'a' points to it


def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

# o/p : a = 30, a = 20 , a = 10

def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

# o/p: a = 30, a = 30, a = 30