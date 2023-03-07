
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


