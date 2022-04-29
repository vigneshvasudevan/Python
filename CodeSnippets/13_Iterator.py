'''
Iterator
An iterator is an object that implements __iter__ and __next__ methods.
An iterator cannot be reusable once all items have been returned.

'''
class Square:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration

        self.current += 1
        return self.current ** 2
    
    
square = Square(5)
for sq in square:
    print(sq)
    
    
'''
Summary:
Iterables: An iterable is an object that you can iterate over.
'''