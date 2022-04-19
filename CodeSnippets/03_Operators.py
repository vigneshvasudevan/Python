'''
Ref: 
https://docs.python.org/3/library/operator.html
https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types


# what is an operator?
Operators are used to carry out an operation say adding two numbers using 
an + operator

# why we need them ?
To perform operations

# how to use them ?
Based on the type of operators we might need to pass one or more operands


# Is there an alterante to it?
Yes, built in functions can be used say x = add(5, 10) is same as x = 5 + 10

'''

'''
-------------------------
Topic: Types of operator
-------------------------
1. Arithemetic
    + for addition
    - for subtraction
    / for division
    * for multiplication
    % for modullo
    // for floor division

2. Bitwise operators
    ~ NOT
    & AND
    | OR
    ^ XOR
    >> Right shift
    << Left shift
    
3. Logical operators
    and 
    or
    not
    
    == equality
    = assignment
    > greater than
    >= greater than or equal to
    < lesser than
    <= lesser than or equal to
    != Not equal to
    
4. Special operators
    : Slice
    in containment operator
    @ matrix multiplication
    
'''



foo = 100
bar = 200
x = 0
baz = foo and x
print(baz)
baz = foo or x 
print(baz)


num = 100; 

# ternary operator
x = "0" if num %2 == 0 else "1"

if num%2 == 0 :
    x = "0"
else :
    x = "1" 
    
