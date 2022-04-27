
def binarySearch(x : list, searchFor : int) -> int:
    if len(x) == 0 :
        return -1

    start = 0
    end = len(x) - 1
    while end >= start:
        mid = (end+start) // 2
        if x[mid] == searchFor :
            return mid

        elif x[mid] > searchFor :
            end = mid - 1
        else:
            start = mid+1

    return -1

print(binarySearch([1,2, 3, 4, 5], 5))


def binarySearchUsingRecursion(x : list, start, end, searchFor : int) -> int:
    if len(x) == 0 or end < start:
        return -1

    mid = (end+start) // 2
    if x[mid] == searchFor :
        return mid
    
    elif x[mid] > searchFor :
        return binarySearchUsingRecursion(x, start, mid - 1, searchFor)
    else:
        return binarySearchUsingRecursion(x, mid+1, end, searchFor)


x = [1,2, 3, 4, 5]
print(binarySearchUsingRecursion(x, 0, len(x)-1, 5))



  
  
  
