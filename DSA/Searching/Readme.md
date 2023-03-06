
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







