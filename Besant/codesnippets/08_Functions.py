# Functions 

'''

# what is a Function?
Function are a way to organize code which can be re-used. It keeps code
modular and helps maintenance

# why we need them ?
When we see same piece of code used at multiple places, we could consider creating a function
and calling it.


How to use them;
Syntax:
def <function name> (argument1, argument2, ...) :
    <logic goes here>
    return <optionally return something from a function>        
'''


# Topic: Function to find maximum of two numbers
def max (a, b):
    if (a > b):
        return a
    return b

# calling 'max' function
x = max(10.1897980, 20.987980)
print("x=" , x)

# Topic: Function to find maximum of two numbers with input type and return type specified
def max2 (a : int , b: int)  -> int:
    if (a > b):
        return a
    return b

x = max2(10.1897980, 20.987980)
print("x=" , x)


# Topic: Function with default args
def power (x, y = 2) :
    return x**y

print("Square of 5 = ", power(5))
print("Cube of 5 = ", power(5, 3))


# Topic: Function with variable length arguments
def min(arr) :
    if type(arr) != list or len(arr) == 0 :
        return None
    
    smallest = arr[0]
    for i in range(1, len(arr), 1):
        if arr[i] < smallest :
            smallest = arr[i]

    return smallest
        
# calling min function passing a list
print("Minimum = ", min([5, 6, 1, 2, 0, 4]))

def minUsingVarLengthArgument(*args) :
    if len(args) == 0 :
        return None
    
    smallest = args[0]
    for i in range(1, len(args), 1):
        if args[i] < smallest :
            smallest = args[i]

    return smallest
        
# calling min function passing a list
print("Minimum = ", minUsingVarLengthArgument(5, 6, 1, 2, 0, 4))



# Topic: Function with variable length keyword arguments
def foo(**kwargs) :
    for key, val in kwargs.items():
        print(key, "=" , val)

foo( x = 100, y = 200)
foo( y = 100, z = 200, a = 100, b = 400)


#Topic: Call by value : Primitive values are passed by value to the function args
def swap(x, y) :
    temp = x
    x = y
    y = x
    
a = 100
b = 200
print("Before swap a =", a)
print("Before swap b =", b)
swap(a, b)
print("After swap a =", a)
print("After swap b =", b)
# here o/p before and after swap will be same since swap is called by value

def swap(x, y) :
    temp = x
    x = y
    y = x
    # returning the swapped value
    return (x, y)

a = 60
b = 70
print("Before swap a =", a)
print("Before swap b =", b)
a, b = swap(a, b)
print("After swap a =", a)
print("After swap b =", b)



#Topic: Call by referrence : All non-primitve value is passed by ref to function arguments

def sort(arr) :
    # selection sort
    for i in range(0, len(arr)-1, 1):
        smallestPos = i
        for j in range(i+1, len(arr), 1):
            if arr[j] < arr[smallestPos]:
                smallestPos = j
                
        if i != smallestPos :
            temp = arr[i]
            arr[i] = arr[smallestPos]
            arr[smallestPos] = temp
  
      
arr = [10, 20, 5, 8, 7 , 15]
print("Before sorting Array = ", arr)
sort(arr) 
print("After sorting Array = ", arr) 

'''
Things to try: 
    1. Write a function which takes one argument & return nth fibonacci
'''

