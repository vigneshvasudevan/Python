'''
What is an Exception: 
Errors detected during execution are called exceptions 
and are not unconditionally fatal.

A classical example to exception is dividing a number by zero

'''


x = 10
y = 0
# put all statements which might cause exceptions under 'try' block
try:
    z = x % y
# On "ZeroDivisionError"
except ZeroDivisionError:
    print("Value error occurred")
# On any other than "ZeroDivisionError" exception say if y = None
except :
    print("something went and not sure what went wrong")  
# Finally block will be called at the end regardless if exception was
# seen or unseen inside 'try'
finally:
    print("inside finally block")
    


# Throwing exceptions using keyword "raise"   
def divide(arg1, arg2):
    if ((type(arg1) == int or type(arg1) == float or type(arg2) == int or type(arg2) == float) and (arg1 != 0 and arg2 != 0)) :
        return arg1/arg2
    else: 
        print("Not a number")
        raise Exception("ValueError")
    
try:
    print(divide(10, "hello"))
except:
    print("oops")
    

# custom exception
class CustomError(Exception):
    pass

raise CustomError


class SalaryNotInRangeError(Exception):
    """Exception raised when salary is less than 5000pm.

    Attributes:
        salary -- input salary which caused the error
        message -- some message
    """

    def __init__(self, salary, message="Minimum wage as per labour law is 5000 pm"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if 5000 > salary :
    raise SalaryNotInRangeError(salary)
