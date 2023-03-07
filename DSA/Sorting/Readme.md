
## 1.Python program to implement insertion sort.

Problem Description
The program sorts a list by insertion sort.

Problem Solution
1. Create a function insertion_sort that takes a list as argument.
2. Inside the function create a loop with a loop variable i that counts from 1 to the length of the list – 1.
3. Set temp equal to the element at index i.
4. Set j equal to i – 1.
5. Create a while loop that runs as long as j is non-negative and temp is smaller than the element at index j.
6. Inside the while loop, set the element at index j + 1 equal to the element at index j and decrement j.
7. After the while loop finishes, set the element at index j + 1 equal to temp.

Program/Source Code
Here is the source code of a Python program to implement insertion sort. The program output is shown below.
```
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The list is passed to the insertion_sort function.
3. The sorted list is displayed.

```
Runtime Test Cases
Case 1:
Enter the list of numbers: 2 4 1 5 8 0
Sorted list: [0, 1, 2, 4, 5, 8]
 
Case 2:
Enter the list of numbers: 5 4 3 2 0 -1
Sorted list: [-1, 0, 2, 3, 4, 5]
 
Case 3:
Enter the list of numbers: 3 4 1 4 5 0 7
Sorted list: [0, 1, 3, 4, 4, 5, 7]
```
## 2.  Python program to implement selection sort.

Problem Description
The program sorts a list by selection sort.

Problem Solution
1. Create a function selection_sort that takes a list as argument.
2. Inside the function create a loop with a loop variable i that counts from 0 to the length of the list – 1.
3. Create a variable smallest with initial value i.
4. Create an inner loop with a loop variable j that counts from i + 1 up to the length of the list – 1.
5. Inside the inner loop, if the elements at index j is smaller than the element at index smallest, then set smallest equal to j.
6. After the inner loop finishes, swap the elements at indexes i and smallest.

Program/Source Code
Here is the source code of a Python program to implement selection sort. The program output is shown below.
```
def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)
```

Program Explanation
1. The user is prompted to enter a list of numbers.
2. The list is passed to the selection_sort function.
3. The sorted list is displayed.

```
Runtime Test Cases
Case 1:
Enter the list of numbers: 3 1 4 5 2 6
Sorted list: [1, 2, 3, 4, 5, 6]
 
Case 2:
Enter the list of numbers: 2 10 5 38 1 7
Sorted list: [1, 2, 5, 7, 10, 38]
 
Case 3:
Enter the list of numbers: 5 3 2 1 0
Sorted list: [0, 1, 2, 3, 5]
```


## 3. Python program to implement bubble sort.

Problem Description
The program sorts a list by bubble sort.

Problem Solution
1. Create a function bubble_sort that takes a list as argument.
2. Inside the function create a loop with a loop variable i that counts from the length of the list – 1 to 1.
3. Create an inner loop with a loop variable that counts from 0 up to i – 1.
4. Inside the inner loop, if the elements at indexes j and j + 1 are out of order, then swap them.
5. If in one iteration of the inner loop there were no swaps, then the list is sorted and one can return prematurely.

Program/Source Code
Here is the source code of a Python program to implement bubble sort. The program output is shown below.
```
def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False
        if no_swap:
            return
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
bubble_sort(alist)
print('Sorted list: ', end='')
print(alist)
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The list is passed to the bubble_sort function.
3. The sorted list is displayed.


```
Runtime Test Cases
Case 1:
Enter the list of numbers: 4 2 38 10 5
Sorted list: [2, 4, 5, 10, 38]
 
Case 2:
Enter the list of numbers: 5 4 3 2 1
Sorted list: [1, 2, 3, 4, 5]
 
Case 3:
Enter the list of numbers: 7 3 1 -5 2 10
Sorted list: [-5, 1, 2, 3, 7, 10]

```

## 4.Python program to implement merge sort.

Problem Description
The program sorts a list by merge sort.

Problem Solution
1. Create a function merge_sort that takes a list and two variables start and end as arguments.
2. The function merge_sort will sort the list from indexes start to end – 1 inclusive.
3. If end – start is not greater than 1, then return.
4. Otherwise, set mid equal to the floor of (start + end)/2.
5. Call merge_sort with the same list and with start = start and end = mid as arguments.
6. Call merge_sort with the same list and with start = mid and end = end as arguments.
7. Call the function merge_list, passing the list and the variables start, mid and end as arguments.
8. The function merge_list takes a list and three numbers, start, mid and end as arguments and assuming the list is sorted from indexes start to mid – 1 and from mid to end – 1, merges them to create a new sorted list from indexes start to end – 1.

Program/Source Code
Here is the source code of a Python program to implement merge sort. The program output is shown below.
```
def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
 
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The list is passed to the merge_sort function.
3. The sorted list is displayed.

```
Runtime Test Cases
Case 1:
Enter the list of numbers: 3 1 5 8 2 5 1 3
Sorted list: [1, 1, 2, 3, 3, 5, 5, 8]
 
Case 2:
Enter the list of numbers: 5 3 2 1 0
Sorted list: [0, 1, 2, 3, 5]
 
Case 3:
Enter the list of numbers: 1
Sorted list: [1]


```
## 5. Python program to implement quicksort.

Problem Description
The program sorts a list by quicksort.

Problem Solution
1. Create a function quicksort that takes a list and two variables start and end as arguments.
2. If end – start is not greater than 1, return.
3. Find the index of the pivot, p by calling the function partition with the list and variables start and end as arguments.
4. Call quicksort with the list and the variables start and p as arguments to sort the list from start to p – 1.
5. Call quicksort with the list, the expression p + 1 and end as arguments to sort the list from p + 1 to end – 1.
6. Define the function partition that takes a list and two variables start and end as arguments.
7. The function parititon uses Hoare’s partition scheme to partition the list.

Program/Source Code
Here is the source code of a Python program to implement quicksort. The program output is shown below.
```
def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)
 
 
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
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)
```
Program Explanation
1. The user is prompted to enter a list of numbers.
2. The list is passed to the quicksort function.
3. The sorted list is displayed.

```
Runtime Test Cases
Case 1:
Enter the list of numbers: 5 2 8 10 3 0 4
Sorted list: [0, 2, 3, 4, 5, 8, 10]
 
Case 2:
Enter the list of numbers: 7 4 3 2 1
Sorted list: [1, 2, 3, 4, 7]
 
Case 3:
Enter the list of numbers: 2
Sorted list: [2]
```

## 6.Python program to implement comb sort.

Problem Description
The program sorts a list by comb sort.

Problem Solution
1. Create a function comb_sort that takes a list as argument.
2. Set gap equal to the length of the list.
3. Choose an appropriate shrink factor. Here shrink = 1.3.
4. Create a while loop that runs as long as there was at least one swap performed in the previous iteration of the loop (or if this is the first iteration of the loop).
5. Set gap to the floor of gap/shrink.
6. If gap becomes less than 1, set it to 1.
7. Perform bubble sort on the list but only compare and swap elements that are at a distance of gap.
8. If gap was not one, then continue the loop even if there weren’t any swaps performed.

Program/Source Code
Here is the source code of a Python program to implement comb sort. The program output is shown below.
```
def comb_sort(alist):
    def swap(i, j):
        alist[i], alist[j] = alist[j], alist[i]
 
    gap = len(alist)
    shrink = 1.3
 
    no_swap = False
    while not no_swap:
        gap = int(gap/shrink)
 
        if gap < 1:
            gap = 1
            no_swap = True
        else:
            no_swap = False
 
        i = 0
        while i + gap < len(alist):
            if alist[i] > alist[i + gap]:
                swap(i, i + gap)
                no_swap = False
            i = i + 1
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
comb_sort(alist)
print('Sorted list: ', end='')
print(alist)
```

Program Explanation
1. The user is prompted to enter a list of numbers.
2. The list is passed to the comb_sort function.
3. The sorted list is displayed.

```
Runtime Test Cases
Case 1:
Enter the list of numbers: 2 8 4 3 7 10 23 4 5
Sorted list: [2, 3, 4, 4, 5, 7, 8, 10, 23]
 
Case 2:
Enter the list of numbers: 5 4 3 2 1
Sorted list: [1, 2, 3, 4, 5]
 
Case 3:
Enter the list of numbers: 3
Sorted list: [3]

```

