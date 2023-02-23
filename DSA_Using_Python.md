
# What is a Data Structure in python?
The Data Structure is a description of how data is organised (stored), modified, and accessed. By specifying how different sorts of data connect to one another, it also develops relationships and forms algorithms. The data structure of any computer language is a crucial concept in algorithmic design.


# What Are the Various Data Structure Types?
The numerous forms of data structures are as follows:

- Lists : Lists are a collection of related objects that are linked to the data items before and after them.

 - Arrays: Arrays are a collection of values with the same value.

- Stacks: LIFO data structures, or stacks, are those in which the element placed last is accessed first.

- Queues: Queues are a first-in-first-out data structure.

- Graphs: In this data structure, data values are stored in nodes connected by edges.

- Trees: Like a linked list, the data values are linked in a hierarchical structure.

- Hash table: A table in which each value is assigned a key and then preserved, making individual values more accessible.

- Heaps: A binary tree data structure that allows you to compare parent and child data values.

# What Applications Do Data Structures Have?
Data structures are useful for a number of things, including:

- Dynamic memory allocation should be implemented.

- Model sets and other types of data

- Network modelling

- Identifying and resolving the most basic issues




#  Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:
```
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
```

Expected Output:
```
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
```

`Solution`

To access a range of items in a list, use the slicing operator :. With this operator, you can specify where to start the slicing, end, and specify the step.

For example, the expression list1[ start : stop : step] returns the portion of the list from index start to index stop, at a step size step.

- for 1st list: Start from the 1st index with step value 2 so it will pick elements present at index 1, 3, 5, and so on
- for 2nd list: Start from the 0th index with step value 2 so it will pick elements present at index 0, 2, 4, and so on

```
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)
```



2: Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Given:
```
list1 = [54, 44, 27, 79, 91, 41]
```

Expected Output:
```
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
```
 `Solution`
 ```
pop(index): Removes and returns the item at the given index from the list.
insert(index, item): Add the item at the specified position(index) in the list
append(item): Add item at the end of the list.
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)

```


## Sequential Search:
The searching algorithms are the algorithms that are used to search a particular value in a data structure such as lists in Python. For example, imagine that you are trying to find a specific card from a deck of cards. You will go through each card in the deck one by one until you find the card you are looking for. Once you got the card you were looking for you will stop. This is how the sequential search algorithm works. Here is how to implement it using Python:
```
def sequential_search(list_, n):
    for i in list_:
        if i == n:
            break
    return True
  
  
elements = range(0, 20)
ss = sequential_search(elements, 4)
print(ss)
```
## Validate Anagrams:
An Anagram is a word or phrase that forms a different word or phrase when the letters of a word are rearranged. For example, the words “despair” and “praised” are anagrams. The validation of anagram words is one of the favourite questions in coding interviews. The idea is to write an algorithm to check if the input word creates a meaningful word when rearranged. So to validate an anagram using Python, we need to input two words and check if word1 in any case matches word2 after rearranging the words. Here is how to validate anagrams using Python:

```
def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(anagram("cinema", "iceman"))
print(anagram("cool", "loco"))
print(anagram("men", "women"))
```


## What exactly is a stack?
A stack is an abstract data type that provides a linear data structure, analogous to a physical stack or pile where objects may only be removed from the top. As a result, item insertion (push) and deletion (pop) take place only at one end of the stack, the top of the stack, and in a certain order: LIFO (Last In First Out) or FILO (First In Last Out) (First In Last Out).

Implementation in Python
```
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in 
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
# uncommenting print(stack.pop())  
# will cause an IndexError 
# as the stack is now empty
```

##  What operations can you do with a stack?
A stack is a linear data structure that works on the same idea as a list, except that in a stack, components are only added and deleted from one end, the TOP. As a result, a stack is known as a LIFO (Last-In-First-Out) data structure, because the last component inserted is the first component removed.
A stack can carry out three basic operations:

1. PUSH: When you use the push action, a new element is added to the stack. The new function is at the top of the priority list. However, before we insert the value, we must first verify if TOP=MAX–1, since if it is, the stack is filled and no more insertions are possible.
2. POP: To remove the topmost member of a stack, use the pop action. We must first verify if TOP=NULL before deleting the item, because if it is, the stack is empty and no further deletions are permitted. You'll get a UNDERFLOW notice if you try to remove a value from a stack that is already empty.



## In Python, how do you add values to an array?
The append(), extend(), and insert (i,x) procedures can be used to add elements to an array.
```
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print(a)
a.extend([4.5,6.3,6.8])
print(a)
a.insert(2,3.8)
print(a)
```
Output:
```
array(‘d’, [1.1, 2.1, 3.1, 3.4])
array(‘d’, [1.1, 2.1, 3.1, 3.4, 4.5, 6.3, 6.8]) array(‘d’, [1.1, 2.1, 3.8, 3.1, 3.4, 4.5, 6.3, 6.8])
```

##  What's the best way to remove values from a Python array?
The pop() and remove() methods can be used to remove elements from an array. The difference between these two functions is that the first returns the removed value, while the second does not.
```
a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print(a.pop())
print(a.pop(3))
a.remove(1.1)
print(a)
```
## Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:
```
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
```
Expected Output:
```
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
```
- To access a range of items in a list, use the slicing operator :. With this operator, you can specify where to start the slicing, end, and specify the step.

- For example, the expression list1[ start : stop : step] returns the portion of the list from index start to index stop, at a step size step.

- for 1st list: Start from the 1st index with step value 2 so it will pick elements present at index 1, 3, 5, and so on
- for 2nd list: Start from the 0th index with step value 2 so it will pick elements present at index 0, 2, 4, and so on

```
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)
```

## Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Given:
```
list1 = [54, 44, 27, 79, 91, 41]
```
Expected Output:
```
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
```


- pop(index): Removes and returns the item at the given index from the list.
- insert(index, item): Add the item at the specified position(index) in the list
- append(item): Add item at the end of the list.
- sample_list = [34, 54, 67, 89, 11, 43, 94]
```
print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)
```
## Python program to implement linear search
```
numbers = [4,2,7,1,8,3,6]
f = 0 #flag
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print("Successful search, the element is found at position", i)
        f = 1
        break
if(f==0):
    print("Oops! Search unsuccessful")
 ```
 
Output:
```
Enter the number to be found out: 7
Successful search, the element is found at position 2
```
## Python program to implement binary search
```
def binarySearch(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            return mid
        elif (numbers[mid] > x):
            return binarySearch(numbers, low, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, high, x)
    else:
        return -1
numbers = [ 1,4,6,7,12,17,25 ]   #binary search requires sorted numbers
x = 7
result = binarySearch(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")
```
Output:
```
Search successful, element found at position  3
```
## Python program to find the odd numbers in an array
```
numbers = [8,3,1,6,2,4,5,9]
count = 0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count = count+1
print("The number of odd numbers in the list are: ", count)
```
Output:
```
The number of odd numbers in the list are:  4
```


##  we will illustrate how to hash a file. We will use the SHA-1 hashing algorithm. The digest of SHA-1 is 160 bits long.
```
# Python program to find the SHA-1 message digest of a file

# importing the hashlib module
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("track1.mp3")
print(message)
```
Output
```
633d7356947eec543c50b76a1852f92427f4dca9
```
