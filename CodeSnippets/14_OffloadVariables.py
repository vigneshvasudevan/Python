# save and load python variables
FILE_PATH = "../logs/myDict.txt"


import pickle
dict1 = {'foo' : 1, 'bar' : 2}
dict2 = {'foo2' : 1, 'bar2' : 2}
file1 = open(FILE_PATH, "wb") 
pickle.dump([dict1, dict2], file1)
#pickle.dump(dict2, file1)
file1.close()

with open(FILE_PATH, 'rb') as f:
    [var1, var2] = pickle.load(f)
    print(var1)
    print(var2)
    f.close()
    

