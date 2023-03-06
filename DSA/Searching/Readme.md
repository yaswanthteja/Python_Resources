
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

## 4.  Python program to select the ith largest element from a list in expected linear time.

Problem Description
The program takes a list and i as input and prints the ith largest element in the list.

Problem Solution
1. Create a function select which takes a list and variables start, end, i as arguments.
2. The function will return the ith largest element in the range alist[start… end – 1].
3. The base case consists of checking whether there is only one element in the list and if so, alist[start] is returned.
4. Otherwise, the list is partitioned using Hoare’s partitioning scheme.
5. If i is equal to the number of elements in alist[pivot… end – 1], call it k, then the pivot is the ith largest element.
6. Otherwise, depending on whether i is greater or smaller than k, select is called on the appropriate half of the list.

Program/Source Code
Here is the source code of a Python program to select the ith largest element from a list in expected linear time. The program output is shown below.
```
def select(alist, start, end, i):
    """Find ith largest element in alist[start... end-1]."""
    if end - start <= 1:
        return alist[start]
    pivot = partition(alist, start, end)
 
    # number of elements in alist[pivot... end - 1]
    k = end - pivot
 
    if i < k:
        return select(alist, pivot + 1, end, i)
    elif i > k:
        return select(alist, start, pivot, i - k)
 
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
3. The ith largest element is found by calling select.
4. The result is displayed.

```
Runtime Test Cases
Case 1:
Enter the list of numbers: 3 1 5 10 7 2 -2
The ith smallest element will be found. Enter i: 2
Result: 7.
 
Case 2:
Enter the list of numbers: 5 4 3 2 1
The ith smallest element will be found. Enter i: 5
Result: 1.
 
Case 3:
Enter the list of numbers: 3
The ith smallest element will be found. Enter i: 1
Result: 3.
```

## 5. Python program to solve the maximum subarray problem using divide and conquer technique.

Problem Description
The program finds a subarray that has the maximum sum within the given array.

Problem Solution
1. Define the function find_max_subarray that takes a list as argument and two indexes, start and end. It finds the maximum subarray in the range [start, end – 1].
2. The function find_max_subarray returns the tuple (l, r, m) where l, r are the left and right indexes of the maximum subarray and m is its sum.
3. The base case is when the input list is just one element (i.e. start == end – 1).
4. Otherwise, the list is divided into two and find_max_subarray is called on both the halves.
5. The maximum subarray is either the maximum subarray of one of the halves or the maximum subarray crossing the midpoint of the two halves.
6. The function find_max_crossing_subarray takes a list as argument and three indexes, start, mid and end and finds the maximum subarray containing mid.

Program/Source Code
Here is the source code of a Python program to find the subarray with maximum sum. The program output is shown below.
```
def find_max_subarray(alist, start, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray in
    A[start:end] with sum m. Here A[start:end] means all A[x] for start <= x <
    end."""
    # base case
    if start == end - 1:
        return start, end, alist[start]
    else:
        mid = (start + end)//2
        left_start, left_end, left_max = find_max_subarray(alist, start, mid)
        right_start, right_end, right_max = find_max_subarray(alist, mid, end)
        cross_start, cross_end, cross_max = find_max_crossing_subarray(alist, start, mid, end)
        if (left_max > right_max and left_max > cross_max):
            return left_start, left_end, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max
 
def find_max_crossing_subarray(alist, start, mid, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray within
    alist with start <= l < mid <= r < end with sum m. The arguments start, mid,
    end must satisfy start <= mid <= end."""
    sum_left = float('-inf')
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i
 
    sum_right = float('-inf')
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right
 
alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The list is passed to find_max_subarray and the returned tuple is stored.
3. The start and end indexes and the sum of the maximum subarray is printed.


```
Runtime Test Cases
Case 1:
Enter the list of numbers: 3 4 -2 3 -10 32 4 -11 7 -3 2
The maximum subarray starts at index 5, ends at index 6 and has sum 36.
 
Case 2:
Enter the list of numbers: 4 -2 3 4 1 4 -5
The maximum subarray starts at index 0, ends at index 5 and has sum 14.
 
Case 3:
Enter the list of numbers: 2
The maximum subarray starts at index 0, ends at index 0 and has sum 2.

```



