# Loops in python

'''

# what is a Loop?


# why we need them ?


# how to use them ?


# Is there an alterante to it?

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
    
    
mylist = [100, 200, 300, 400, 500, 100]
for i in range(0, len(myList), 1):
    if i == 3:
        break
    print(myList[i])
    
# o/p: 100 200 300 400 500

for i in range(len(myList)-1, -1, -1)
    print(myList[i])

# o/p : 500, 400, 300, 200, 100
//statements will be executed after for loop

i = 0
while (i < len(myList)) :
    print(myList[i])
    i += 1 -> i = i +1 
    
i = len(myList)-1
while (i >=0) :
    print(myList[i])
    i = i -1 -> i -=1


x  = {100, 200, 300, 400, 500}
for i in x :
    print(i)
    

x = {100: "foo", 200:"bar", 300:"baz"}
for i in x :
    print(x[i])


for key, val in x.items() :
    print(key,val)
    or
    print(key,x[key])

num = 100
# start from 1 go until 'num' and check if it's even or odd
num = 100
oddCounter = 0
evenCounter = 0
for i in range(1, num, 1):
    if i % 2 == 0:
        evenCounter +=1 # evenCounter = evenCounter + 1
        #print("Even")
    else :
        oddCounter += 1
        #print("Odd")


for i in range(num-1, 0, -1)
print("Found even numbers = ", evenCounter)
print("Found odd numbers = ", oddCounter)

num = 100
i = 1
while i < num :
    if i % 2 == 0 :
        print("...")
    else :
        print(".....")
    i += 1 # i = i +1
'''

# For 
myList = list([100, 70, 85])
#print(myList)

for i in range(len(myList)):
    # start = 0, stops = len(mylist) which is nothing but 3, increement by 1 
    print(myList[i])


i = 0
while i < len(myList):
    print(myList[i])
    i = i + 1 # i += 1
    
    
x = (100, 70, 85)
for i in range(len(x)):
    print(x[i])
    
    
knights = {'x': 'foo', 'y': 'bar'}
for k in knights:
    print(knights[k])



'''
# while
myList = list([100, 70, 85])
i = 0
while i < len(myList) :
    print(myList[i])
    
    
'''
    
# exercise problem: any sorting algo in python ; time & space complexity ; selection, bubble, insertion , merge, quick sort


