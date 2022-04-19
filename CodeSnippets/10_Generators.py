
'''
# what is a Generator?
Generator is used for creating a iterator

# why we need them ?
Generators are much more efficient both (in execution and memory) than simple functions
'''
# Topic: Generator

# classical way to find sqaure of all 'nums'
arr = [1, 2, 3, 4, 5]
def square(nums):
    mySquare = []
    for i in nums:
        mySquare.append(i*i)
    return mySquare

my_nums = square(arr)
print("myNums is of type %s" %(type(my_nums)))
print(my_nums)

# Using generator approach
def squareUsingGenerator(nums):
    for i in nums:
       yield (i*i)

mySquare = squareUsingGenerator(arr)
print(next(mySquare))
print(next(mySquare))
print(next(mySquare))
print(next(mySquare))
print(next(mySquare))



# Example to validate if generators are efficient
import os, psutil
import random
import time

names = ['foo', 'bar', 'baz', 'hi', 'hello', 'there']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


process = psutil.Process(os.getpid())
print("Mem usgae at Start: " ,process.memory_info().rss)  # in bytes 

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


t1 = time.time()
people = people_list(10000000)
t2 = time.time()

process = psutil.Process(os.getpid())
print("======== Usual way to generate 1million records =========== ")
print("Mem usage after: " , process.memory_info().rss)  # in bytes 
print('Took %d Seconds for program' % int(t2-t1))


t1 = time.time()
people = people_generator(10000000)
t2 = time.time()

process = psutil.Process(os.getpid())
print("======== Using generator =========== ")
print("Mem usage after: " , process.memory_info().rss)  # in bytes 
print('Took %d Seconds for program' % int(t2-t1))


'''
co-routine:

Diff b/w generators and co-routine: generators are data producers where coroutines 
are data consumers.

'''

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print("Found a phrase having ",  pattern)
            
search = grep('coroutine')
next(search)
# Output: Searching for "coroutine"
search.send("This is a simple string passed to yield")
search.send("Another string passed to line number 101")
search.send("Phrase containing coroutine is now being sent")
# Output: Found a phrase having coroutine