'''
# what is a collection?
It's a flavour to vanilla collections in python i.e. (List, tuple, set,dict).
It is found under "collection" module
'''


'''
----------------------------
Topic: named Tuple
----------------------------
'''
from collections import namedtuple
rbgCode = namedtuple('rbgCode', ["Red", "Blue", "Green"])
DarkGreen = rbgCode(Red = 0, Blue= 0, Green= 255)
# this is much better than -> rgbCode = (0, 0, 255) since this doesn't 
# tell us which one belongs to which color say 255 belongs to green or red or blue
print("percentage of red in dark green =", DarkGreen[0])
print("percentage of red in dark green =", DarkGreen[1])
print("percentage of red in dark green =", DarkGreen[2])


'''
-------------------------------
Topic: ordered dict

Sorts the elements in dict by key
--------------------------------
'''

from collections import OrderedDict
ordDict = OrderedDict({2: "foo" , 1 : "bar"})
print(ordDict)
ordDict.update({2 :"baz"})
print(ordDict)



'''
-------------------------------
Topic: Chain map
clubs two dict into one
--------------------------------
'''
from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print("Chained dict = ", ChainMap(adjustments, baseline))


'''
-------------------------------
Topic: Counter
Type of dictionary where elements are stored as dictionary keys 
and their counts are stored as dictionary values
--------------------------------
'''

from collections import Counter
fruitCart = Counter(orange = 2, apple = 4, mango=0, avocado = -2)
print(sorted(fruitCart.elements()))
# output : ['apple', 'apple', 'apple', 'apple', 'orange', 'orange']


'''
-------------------------------
Topic: Default dict
Using list as the default_factory, it is easy to group a sequence 
of key-value pairs into a dictionary of lists
--------------------------------
'''

from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
    
print(sorted(d.items()))

# output: [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]