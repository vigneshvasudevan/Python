'''

# what is a conditional statement?


# why we need them ?


# how to use them ?


# Is there an alterante to it?

'''
# syntax: 
# if <condition1> <condition2> ...<conditionN> :
    #logic goes here
#elif <condition1> <condition2> ... <conditionN> :
    # logic goes here
#elif <condition1> <condition2> ... <conditionN> :
    # logic goes here
.
.
.

# else :
    # some logic goes here>

# given a number, check if one or more digits in the number is '5'

num = 100

if num % 2 == 0 or num% 3 ==0 :
    print("number is either divisible by 2 or 3")
else:
    print("Number is niether divisble by 2 nor by 3")


num = 101
x = num % 5

if x == 0 :
    print("kfjhfksj")
elif x < 2 :
    print("")
else :
    print("")




if (num % 2 == 0 or num % 3 == 0) :
    print("")

reminder = num %2
match reminder :
    case 0, 1:
        print('its even')
    case 1:
        print("it's odd")
        
reminder = num %3

match reminder :
    case 0:
        print("divisble by 3")
    case _:
        print("Not...")


#if-else & switch case statements


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