
'''
# what is a class?
Class is an extensible template, representing skeleton of an entity.

# why we need them ?
Class is the basic element of Object oriented paradigm

'''

# A complex number class having object variable 'r' and 'i'
class Complex:
    # private variable by convention is always prefixed with double underscore
    __privateVar = 100
    # variable outside the constructor is by default static or class variable
    staticVariable = 200
    
    # constructor
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
     
    # object method, here the argument 'self' indicates the object itself
    def myprint(self) :
        print(self.r, self.i)
        
    # class function
    def foo():
        print("Hello world")
    
    # overloading 'len' operator
    def __len__(self) -> int:
        print("foo bar")
        return 0
    
    # overload add operator
    def __add__(self, obj):
        return Complex(self.r + obj.r, self.i + obj.i)
    
    # public method accessing private function and variable
    def getStaticPrivateVar(self) :
        self.__privateMethod()
        return Complex.__privateVar
    
    # Private method can be called only via 
    # other public methods/function implictily
    def __privateMethod(self):
        print("Im a private method")
        

#Creating an instance of class 'complex', this will call the constructor
c1 = Complex(3.0, -4.5)
print(type(c1))
# Accessing static/class variable
print(Complex.staticVariable)
# Modifying public class variables using object
c1.i = 100
c1.r = 200
#Calling class function
Complex.foo()
#calling object method
c1.myprint()
# Complex.__privateVar = 100 is illegal as __privateVar is private
c2 = Complex(-10, 2)
# c1 + c2 statement will call overloaded 'add' method
c3 = c1 + c2


# Inheriting class 'complex'
class AnotherClass(Complex):
    
    # calling base class constructor from child class using 'super' keyword
    def __init__(self, realpart, imagpart):
        super().__init__(realpart, imagpart)
    #overriding base class implementation
    def myprint(self) :
        print("Overriding base class definition")
        print(self.r, self.i)
   
obj = AnotherClass(10, 20)
# Calls overloaded 'myprint' method
obj.myprint()
# Accesing parent class method
obj.getStaticPrivateVar()

'''
Things to try:
A -> B -> C : multi-level inheritance; how do we call A's constructor from C
A, B are independent class; B, A -> C : multiple inheritance, where c inherits both B & A; how do we call A's constructor from C
'''

