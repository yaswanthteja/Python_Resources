
What is a Data Structure in python?
The Data Structure is a description of how data is organised (stored), modified, and accessed. By specifying how different sorts of data connect to one another, it also develops relationships and forms algorithms. The data structure of any computer language is a crucial concept in algorithmic design.


What Are the Various Data Structure Types?
The numerous forms of data structures are as follows:

- Lists : Lists are a collection of related objects that are linked to the data items before and after them.

 - Arrays: Arrays are a collection of values with the same value.

- Stacks: LIFO data structures, or stacks, are those in which the element placed last is accessed first.

- Queues: Queues are a first-in-first-out data structure.

- Graphs: In this data structure, data values are stored in nodes connected by edges.

- Trees: Like a linked list, the data values are linked in a hierarchical structure.

- Hash table: A table in which each value is assigned a key and then preserved, making individual values more accessible.

- Heaps: A binary tree data structure that allows you to compare parent and child data values.





# : Create a list by picking an odd-index items from the first list and even index items from the second
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
