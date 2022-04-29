
'''
What is a process?
A program in execution is usually referred as process
Multiprocessing is the use of two or more central processing 
units (CPUs) within a single computer system

'''
#An example without multi processing
import time

def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')

tic = time.time()
sleepy_man()
sleepy_man()
toc = time.time()

print('Done in {:.4f} seconds'.format(toc-tic))


import multiprocessing

def sleepy_man2():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')

tic = time.time()
p1 =  multiprocessing.Process(target= sleepy_man2)
p2 =  multiprocessing.Process(target= sleepy_man2)
p1.start()
p2.start()
toc = time.time()

print('Done in {:.4f} seconds'.format(toc-tic))


# Ref: https://www.analyticsvidhya.com/blog/2021/04/a-beginners-guide-to-multi-processing-in-python/
