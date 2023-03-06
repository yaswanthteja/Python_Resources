
## 1.  Python program to implement linear search.

Problem Description
The program takes a list and key as input and finds the index of the key in the list using linear search.

Problem Solution
1. Create a function linear_search that takes a list and key as arguemnts.
2. A loop iterates through the list and when an item matching the key is found, the corresponding index is returned.
3. If no such item is found, -1 is returned.

Program/Source Code
Here is the source code of a Python program to implement linear search. The program output is shown below.
```
def linear_search(alist, key):
    """Return index of key in alist. Return -1 if key not present."""
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1
 
 
alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
 
index = linear_search(alist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The user is then asked to enter a key to search for.
3. The list and key is passed to linear_search.
4. If the return value is -1, the key is not found and a message is displayed, otherwise the index of the found item is displayed.

```
Runtime Test Cases
Case 1:
Enter the list of numbers: 5 4 3 2 1 10 11 2
The number to search for: 1
1 was found at index 4.
 
Case 2:
Enter the list of numbers: 5 2 1 5 -3
The number to search for: 2
2 was found at index 1.
 
Case 3:
Enter the list of numbers: 3 5 6
The number to search for: 2
2 was not found.


```

## 2.  Python program to implement binary search with recursion.

Problem Description
The program takes a list and key as input and finds the index of the key in the list using binary search.

Problem Solution
1. Create a function binary_search that takes a list and the variables start, end and key as arguments. The function searches for the key in the range [start… end – 1].
2. The base case consists of testing whether start is less than end. If not, -1 is returned.
3. mid is calculated as the floor of the average of start and end.
4. If the element at index mid is less than key, binary_search is called again wit start=mid + 1 and if it is more than key, it is called with end=mid. Otherwise, mid is returned as the index of the found element.

Program/Source Code
Here is the source code of a Python program to implement binary search using recursion. The program output is shown below.
```
def binary_search(alist, start, end, key):
    """Search key in alist[start... end - 1]."""
    if not start < end:
        return -1
 
    mid = (start + end)//2
    if alist[mid] < key:
        return binary_search(alist, mid + 1, end, key)
    elif alist[mid] > key:
        return binary_search(alist, start, mid, key)
    else:
        return mid
 
 
alist = input('Enter the sorted list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
 
index = binary_search(alist, 0, len(alist), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The user is then asked to enter a key to search for.
3. The list and key is passed to binary_search with start=0 and end=length of the list.
4. If the return value is -1, the key is not found and a message is displayed, otherwise the index of the found item is displayed.

```

Runtime Test Cases
Case 1:
Enter the sorted list of numbers: 4 5 6 7 8 9 10
The number to search for: 9
9 was found at index 5.
 
Case 2:
Enter the sorted list of numbers: 3 4 5 10
The number to search for: 8
8 was not found.
 
Case 3:
Enter the sorted list of numbers: 7
The number to search for: 

```

## 3.  Python program to select the ith smallest element from a list in expected linear time.

Problem Description
The program takes a list and i as input and prints the ith smallest element in the list.

Problem Solution
1. Create a function select which takes a list and variables start, end, i as arguments.
2. The function will return the ith smallest element in the range alist[start… end – 1].
3. The base case consists of checking whether there is only one element in the list and if so, alist[start] is returned.
4. Otherwise, the list is partitioned using Hoare’s partitioning scheme.
5. If i is equal to the number of elements in alist[start… pivot], call it k, then the pivot is the ith smallest element.
6. Otherwise, depending on whether i is greater or smaller than k, select is called on the appropriate half of the list.

Program/Source Code
Here is the source code of a Python program to select the ith smallest element from a list in expected linear time. The program output is shown below.
```
def select(alist, start, end, i):
    """Find ith smallest element in alist[start... end-1]."""
    if end - start <= 1:
        return alist[start]
    pivot = partition(alist, start, end)
 
    # number of elements in alist[start... pivot]
    k = pivot - start + 1
 
    if i < k:
        return select(alist, start, pivot, i)
    elif i > k:
        return select(alist, pivot + 1, end, i - k)
 
    return alist[pivot]
 
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
 
 
alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
i = int(input('The ith smallest element will be found. Enter i: '))
 
ith_smallest_item = select(alist, 0, len(alist), i)
print('Result: {}.'.format(ith_smallest_item))
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The user is then asked to enter i.
3. The ith smallest element is found by calling select.
4. The result is displayed.


```
Runtime Test Cases
Case 1:
Enter the list of numbers: 3 5 10 2 -1 0 2
The ith smallest element will be found. Enter i: 2
Result: 0.
 
Case 2:
Enter the list of numbers: 7
The ith smallest element will be found. Enter i: 1
Result: 7.
 
Case 3:
Enter the list of numbers: 5 4 3 2 1
The ith smallest element will be found. Enter i: 5
Result: 5.


```





