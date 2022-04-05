'''
Problem: Consider an array of size 'N', sort the array in ascending order
'''

'''
Selection sort algo:
1. let i be 0 (start element)
2. Assume that element found at 'i'th position is the 'i'th smallest element
3. Scan all elements to the right side of 'i' to find 'i'th smallest element position
4. swap arr[i] with arr[smallestElemPosition]
5. increement 'i'
6. If i < N-1, repeat step2, stop otherwise
'''

arr = [10, 20, 15, 8, 7 , 25]
print("Before sorting Array = ", arr)

# selection sort
for i in range(0, len(arr)-1, 1):
    smallestPos = i
    for j in range(i+1, len(arr), 1):
        if arr[j] < arr[smallestPos]:
            smallestPos = j
            
    if i != smallestPos :
        temp = arr[i]
        arr[i] = arr[smallestPos]
        arr[smallestPos] = temp
    
print("After sorting Array = ", arr)


'''
Bubble sort algo:
1. let i be N-1 (start element)
2. check if i >= 0 and if true let j = 0
3. check if j < i , continue with step4 if true, increeement 'i' otherwise and repeat step2
4. check if arr[j] > arr[j+1], swap arr[j] & arr[j+1]
5. increement j, repeat step3
'''

# Bubble sort
arr = [10, 20, 15, 8, 7 , 25]
print("Before sorting Array = ", arr)
for i in range(len(arr) -1 , 0, -1):
    for j in range(0, i, 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            
print("After sorting Array = ", arr)
