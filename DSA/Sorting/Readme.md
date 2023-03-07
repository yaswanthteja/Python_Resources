
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

