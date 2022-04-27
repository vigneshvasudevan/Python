'''

# what is a decorator?
A decorator takes in a function, adds some functionality and returns it
This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time


How does it work?
Basically, a decorator takes in a function, adds some functionality and returns it.
'''


# simple closure
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")



# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()

'''
Output:

I got decorated
I am ordinary

'''


'''
def divide(a, b):
    return a/b
    
    
divide(2,0) will result in below error
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
'''

#Now let's make a decorator to check for this case that 
# will cause the error.

def smart_divide(func):
    def inner(a, b):
        print("divide", a, "by", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)
    
# @smart_divide divide(5, 10) is nothing but 
# decoratedDivide = smart_divide(divide(a = 5, b=10)); decoratedDivide(5, 10)