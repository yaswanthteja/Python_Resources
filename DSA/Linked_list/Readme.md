

## 1.This is a Python program to create a linked list and display its elements.

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

## 2.This is a Python program to remove duplicates from a linked list.

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

## 3. two linked lists are the same.

Problem Description
The program creates two linked lists using data items input from the user and checks whether they are the same.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variables head and last_node.
3. The variable head points to the first element in the linked list while last_node points to the last.
4. Define methods append and display inside the class LinkedList to append data and display the linked list respectively.
5. Define a function is_equal which takes two linked lists as arguments.
6. The function is_equal returns True only if the two linked lists are of the same length and contain the same data items.
7. Create two instances of LinkedList and append data to it.
8. Check whether they are the same.

Program/Source Code
Here is the source code of a Python program to check whether two linked lists are the same. The program output is shown below.
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
 
 
def is_equal(llist1, llist2):
    current1 = llist1.head
    current2 = llist2.head
    while (current1 and current2):
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    if current1 is None and current2 is None:
        return True
    else:
        return False
 
 
llist1 = LinkedList()
llist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))
 
if is_equal(llist1, llist2):
    print('The two linked lists are the same.')
else:
    print('The two linked list are not the same.', end = '')
```
Program Explanation
1. Two instances of LinkedList are created.
2. The user is prompted to enter the data items for the two lists.
3. The function is_equal determines whether the two linked lists are the same.
4. This result is then displayed.

```
Runtime Test Cases
Case 1:
Please enter the elements in the first linked list: 5 8 10 12
Please enter the elements in the second linked list: 5 8 10 12
The two linked lists are the same.
 
Case 2:
Please enter the elements in the first linked list: 12 3 4 5 0
Please enter the elements in the second linked list: 12 3
The two linked list are not the same.
 
Case 3:
Please enter the elements in the first linked list: 4 1
Please enter the elements in the second linked list: 2 19 4
The two linked list are not the same.
```


## 4. Python program to solve the Josephus problem using a linked list.

Problem Description
The program uses a circular single linked list to solve the Josephus problem.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variable head.
3. The variable head points to the first element in the circular linked list.
4. Define methods get_node, get_prev_node, insert_after, insert_before, insert_at_end, remove and append.
5. The method get_node takes an index as argument and traverses the list from a specified node that many times to return the node at that index. The specified node is given by the second argument passed to it.
6. The method get_prev_node takes a reference node as argument and returns the previous node.
7. The methods insert_after and insert_before insert a node after or before some reference node in the list.
8. The methods insert_at_end inserts a node at the last position of the list.
9. The method remove takes a node as argument and removes it from the list.
10. The method appends a node with the data item passed to the end of the list.
11. Define function has_one_node which returns True only if the circular list passed to it has only one node.
12. Define function get_josephus_solution which takes a circular linked list and a number k as argument.
13. The function get_josephus_solution returns the solution to the Josephus problem where the people are represented by the nodes in the circular linked list and every kth person is executed.
14. Create an instance of CircularLinkedList and find the solution to the Josephus problem for a given k.

Program/Source Code
Here is the source code of a Python program to solve the Josephus problem using a linked list. The program output is shown below.
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, data):
        node = Node(data)
        self.insert_at_end(node)
 
    def get_node(self, index, start):
        if self.head is None:
            return None
        current = start
        for i in range(index):
            current = current.next
        return current
 
    def get_prev_node(self, ref_node):
        if self.head is None:
            return None
        current = self.head
        while current.next != ref_node:
            current = current.next
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)
 
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            self.insert_before(self.head, new_node)
 
    def remove(self, node):
        if self.head.next == self.head:
            self.head = None
        else:
            prev_node = self.get_prev_node(node)
            prev_node.next = node.next
            if self.head == node:
                self.head = node.next
 
 
def has_one_node(cllist):
    if cllist.head.next == cllist.head:
        return True
    else:
        return False
 
 
def get_josephus_solution(cllist, k):
    if cllist.head is None:
        return None
    start = cllist.head
    while not has_one_node(cllist):
        to_remove = cllist.get_node(k - 1, start)
        start = to_remove.next
        cllist.remove(to_remove)
    return cllist.head.data
 
 
a_cllist = CircularLinkedList()
n = int(input('Input number of people: '))
k = int(input('The kth person will be executed. Input k: '))
for i in range(1, n + 1):
    a_cllist.append(i)
 
ans = get_josephus_solution(a_cllist, k)
print('The person at position {} won\'t be killed.'.format(ans))
```
Program Explanation
1. The user is prompted to enter the values of n and k.
2. An instance of CircularLinkedList is created with n nodes where the nodes have values from 1 to n.
3. The function get_josephus_solution is called with the circular linked list and k as arguments.
4. The return value is the position of the person who won’t be executed in the Josephus problem.

```
Runtime Test Cases
Case 1:
Input number of people: 5
The kth person will be executed. Input k: 3
The person at position 4 won't be killed.
 
Case 2:
Input number of people: 15
The kth person will be executed. Input k: 7
The person at position 5 won't be killed.
 
Case 3:
Input number of people: 8
The kth person will be executed. Input k: 2
The person at position 1 won't be killed.
```
