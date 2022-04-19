'''
# what is a conditional statement?
Execute statement conditionally rather doing it always
'''

'''
----------------------------
Topic: If-else

syntax: 
if <condition1> <condition2> ...<conditionN> :
    #logic goes here
elif <condition1> <condition2> ... <conditionN> :
    # logic goes here
elif <condition1> <condition2> ... <conditionN> :
    # logic goes here
else :
    # some logic goes here

----------------------------
'''

num = 100
if num % 2 == 0 or num% 3 ==0 :
    print("number is either divisible by 2 or 3")
else:
    print("Number is niether divisble by 2 nor by 3")


# Ternary operator using if -else
x = "even" if num % 2 == 0 else "odd"
print(x)


# switch case supported from 3.10.x pthon
reminder = num %2
match reminder :
    case 0:
        print('its even')
    case 1:
        print("it's odd")
        
reminder = num %3

match reminder :
    case 0:
        print("divisble by 3")
    case _:
        print("Not...")


# swith case from python 3.10
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet" # This is the default case
        

'''
Things to try:
    1. Given a number check if that number contains 6 as it digit
'''