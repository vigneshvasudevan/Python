'''

# what is a collection?


# why we need them ?


# how to use them ?


# Is there an alterante to it?

'''

'''
from collections import namedtuple
record = namedtuple('studentrec', ['rollnum', 'name'])
stu1 = record(100, "foo")
print(stu1[0])
print(stu1[1])

from collections import namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55,155,255)
white = Color(255,255,255)

print(color.blue)

# tuple
color = (55,155,255)
# dictionary
color = {'red': 55, 'green': 155, 'blue': 255}

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(blue=55,green=155,red=255)
'''

from collections import OrderedDict
ordDict = OrderedDict({2: "foo" , 1 : "bar"})
print(ordDict)
ordDict.update({2 :"baz"})
print(ordDict)

'''

myDict = {101: "foo", 102:"bar", 100:"baz"}
myDict[101] = "hello"
print(myDict)

'''