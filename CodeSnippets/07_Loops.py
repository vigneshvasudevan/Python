'''
# what is a Loop?
Do something over and over and again. 

'''


'''
----------------------------
Topic: For, while loop

syntax:

for i in range(start, stop, step):
    your logic goes here
    
# lower to upper bound
i = start
while(i<stop) :
    logic goes here
    i = i + step
    
# upper bound to lower bound
i = stop -1
while (i >= start) :
    logic goes here
    i = i - step
    
----------------------------
'''



'''
------------------------------------------------------------------
Topic: break, continue inside loops
------------------------------------------------------------------
'''
myList = [100, 200, 300, 400, 500, 100]

for i in range(0, len(myList), 1):
    print(myList[i])    
# output: 100, 200, 300, 400, 500, 100

for i in range(0, len(myList), 1):
    if i == 3:
        continue
    print(myList[i])
# output: 100, 200, 300, 500, 100
  
for i in range(0, len(myList), 1):
    if i == 3:
        break
    print(myList[i])
# output: 100 200 300 


'''
-----------------------------------------------
Topic: Iterate List/tuple using For and while
-----------------------------------------------
'''
for i in range(0, len(myList), 1):
    print(myList[i])    
# output: 100, 200, 300, 400, 500, 100

i = 0
while (i < len(myList)) :
    print(myList[i])
    i += 1
# output: 100, 200, 300, 400, 500, 100
   
for i in range(len(myList)-1, -1, -1):
    print(myList[i])

# output : 100, 500, 400, 300, 200, 100

i = len(myList)-1
while (i >=0) :
    print(myList[i])
    i = i -1
# output : 100, 500, 400, 300, 200, 100


'''
-----------------------------------------------
Topic: Iterate sets & dict
-----------------------------------------------
'''

y = {100, 200, 300}
for i in y :
    print(i)
# output : 100 200 300

x = {100: "foo", 200:"bar", 300:"baz"}
for i in x :
    print(x[i])
# output: foo bar baz


for key, val in x.items() :
    print(key,val)
# output: 100 foo 200 bar 300 baz


'''
-----------------------------------------------------
Topic: Examples
1. Find all even and odd numbers starting from 1 to N 
-----------------------------------------------------
'''
num = 100
# start from 1 go until 'num' and check if it's even or odd
num = 100
odd = []
even = []
for i in range(1, num+1, 1):
    if i % 2 == 0:
        even.append(i)
    else :
        odd.append(i)



'''
Things to try: 
    1. Find all numbers starting from 1 to N which has 5 as a digit
    2. Implement selection sort, bubble sort & insertion sort
'''

