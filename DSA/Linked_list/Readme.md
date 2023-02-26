

## This is a Python program to create a linked list and display its elements.

Problem Description
The program creates a linked list using data items input from the user and displays it.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variables head and last_node.
3. The variable head points to the first element in the linked list while last_node points to the last.
4. Define methods append and display inside the class LinkedList to append data and display the linked list respectively.
5. Create an instance of LinkedList, append data to it and display the list.

Program/Source Code
Here is the source code of a Python program to create a linked list and display its elements. The program output is shown below.
```
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
```
Program Explanation
1. An instance of LinkedList is created.
2. The user is asked for the number of elements they would like to add. This is stored in n.
3. Using a loop, data from the user is appended to the linked list n times.
4. The linked list is displayed.

```
Runtime Test Cases
Case 1:
How many elements would you like to add? 5
Enter data item: 3
Enter data item: -2
Enter data item: 1
Enter data item: 5
Enter data item: 0
The linked list: 3 -2 1 5 0 
 
Case 2:
How many elements would you like to add? 1
Enter data item: 6
The linked list: 6 
 
Case 3:
How many elements would you like to add? 4
Enter data item: 2
Enter data item: 9
Enter data item: 3
Enter data item: 2
The linked list: 2 9 3 2
```

## This is a Python program to remove duplicates from a linked list.

Problem Description
The program creates a linked list and removes duplicates from it.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variables head and last_node.
3. The variable head points to the first element in the linked list while last_node points to the last.
4. Define methods append, get_prev_node, remove and display.
5. The method append takes a data item as argument and appends a node with that data item to the list.
6. The method get_prev_node takes a reference node as argument and returns the previous node. It returns None when the reference node is the first node.
7. The method remove takes a node as argument and removes it from the list.
8. The method display traverses the list from the first node and prints the data of each node.
9. Define a function remove_duplicates which takes a linked list as argument and removes duplicates from it.
10. The function remove_duplicates uses two nested loops to remove duplicate nodes.
11. Create an instance of LinkedList, remove duplicate nodes and display the list.

Program/Source Code
Here is the source code of a Python program to remove duplicates from a linked list. The program output is shown below.
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        data = current1.data
        current2 = current1.next
        while current2:
            if current2.data == data:
                llist.remove(current2)
            current2 = current2.next
        current1 = current1.next
 
 
a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
remove_duplicates(a_llist)
 
print('The list with duplicates removed: ')
a_llist.display()
```
Program Explanation
1. An instance of LinkedList is created.
2. The user is prompted to enter the data items for the list.
3. The function remove_duplicates is called to remove duplicates from the list.
4. The linked list is displayed.
```
Runtime Test Cases
Case 1:
Please enter the elements in the linked list: 1 5 2 1 4 5 4 5
The list with duplicates removed: 
1 5 2 4 
 
Case 2:
Please enter the elements in the linked list: 3 4 1
The list with duplicates removed: 
3 4 1 
 
Case 3:
Please enter the elements in the linked list: 1 3 3 14 5 1 0
The list with duplicates removed: 
1 3 14 5 0
```

