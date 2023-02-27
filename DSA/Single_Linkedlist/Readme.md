
##  1. Python program to illustrate the operations of a singly linked list.

Problem Description
The program creates a singly linked list and presents the user with a menu to perform various operations on the list.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variable head.
3. The variable head points to the first element in the singly linked list.
4. Define methods get_node, get_prev_node, insert_after, insert_before, insert_at_beg, insert_at_end, remove and display.
5. get_node takes an index as argument and traverses the list from the first node that many times to return the node at that index.
6. get_prev_node takes a reference node as argument and returns the previous node. It returns None when the reference node is the first node.
7. The methods insert_after and insert_before insert a node after or before some reference node in the list.
8. The methods insert_at_beg and insert_at_end insert a node at the first or last position of the list.
9. The method remove takes a node as argument and removes it from the list.
10. The method display traverses the list from the first node and prints the data of each node.
11. Create an instance of LinkedList and present the user with a menu to perform operations on the list.

Program/Source Code
Here is the source code of a Python program to create a singly linked list and illustrate its operations. The program output is shown below.
```
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)
 
    def insert_at_beg(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
 
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
 
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
 
 
a_llist = LinkedList()
 
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
 
while True:
    print('The list: ', end = '')
    a_llist.display()
    print()
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
 
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_llist.insert_at_beg(new_node)
            elif position == 'end':
                a_llist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_llist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_llist.insert_before(ref_node, new_node)
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_llist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_llist.remove(node)
 
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of LinkedList is created.
2. The user is presented with a menu to perform various operations on the list.
3. The corresponding methods are called to perform each operation.

```
Runtime Test Cases
Case 1:
Menu
insert <data> after <index>
insert <data> before <index>
insert <data> at beg
insert <data> at end
remove <index>
quit
The list: 
What would you like to do? insert 7 at beg
The list: 7 
What would you like to do? insert 3 at end
The list: 7 3 
What would you like to do? insert 1 after 0
The list: 7 1 3 
What would you like to do? insert 9 before 2
The list: 7 1 9 3 
What would you like to do? remove 2
The list: 7 1 3 
What would you like to do? insert 12 at end
The list: 7 1 3 12 
What would you like to do? remove 0
The list: 1 3 12 
What would you like to do? quit
 
Case 2:
Menu
insert <data> after <index>
insert <data> before <index>
insert <data> at beg
insert <data> at end
remove <index>
quit
The list: 
What would you like to do? insert 5 after 0
No such index.
The list: 
What would you like to do? insert 3 at end
The list: 3 
What would you like to do? insert 1 after 0
The list: 3 1 
What would you like to do? insert 2 before 1
The list: 3 2 1 
What would you like to do? insert 0 at end
The list: 3 2 1 0 
What would you like to do? remove 3
The list: 3 2 1 
What would you like to do? remove 2
The list: 3 2 
What would you like to do? quit
```

## 2. Python program to demonstrate a circular single linked list.

Problem Description
The program creates a circular single linked list and presents the user with a menu to perform various operations on the list.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class CircularLinkedList with instance variable head.
3. The variable head points to the first element in the circular single linked list.
4. Define methods get_node, get_prev_node, insert_after, insert_before, insert_at_beg, insert_at_end, remove and display.
5. get_node takes an index as argument and traverses the list from the first node that many times to return the node at that index. It stops if it reaches the first node again.
6. get_prev_node takes a reference node as argument and returns the previous node.
7. The methods insert_after and insert_before insert a node after or before some reference node in the list.
8. The methods insert_at_beg and insert_at_end insert a node at the first or last position of the list.
9. The method remove takes a node as argument and removes it from the list.
10. The method display traverses the list from the first node and prints the data of each node. It stops when it reaches the first node again.
11. Create an instance of CircularLinkedList and present the user with a menu to perform operations on the list.

Program/Source Code
Here is the source code of a Python program to demonstrate a circular single linked list. The program output is shown below.
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def get_node(self, index):
        if self.head is None:
            return None
        current = self.head
        for i in range(index):
            current = current.next
            if current == self.head:
                return None
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
 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.head = new_node
 
    def remove(self, node):
        if self.head.next == self.head:
            self.head = None
        else:
            prev_node = self.get_prev_node(node)
            prev_node.next = node.next
            if self.head == node:
                self.head = node.next
 
    def display(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.head:
                break
 
 
a_cllist = CircularLinkedList()
 
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
 
while True:
    print('The list: ', end = '')
    a_cllist.display()
    print()
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
 
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_cllist.insert_at_beg(new_node)
            elif position == 'end':
                a_cllist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_cllist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_cllist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_cllist.insert_before(ref_node, new_node)
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_cllist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_cllist.remove(node)
 
    elif operation == 'quit':
        break
 ```
Program Explanation
1. An instance of CircularLinkedList is created.
2. The user is presented with a menu to perform various operations on the list.
3. The corresponding methods are called to perform each operation.

```
Runtime Test Cases
Case 1:
Menu
insert <data> after <index>
insert <data> before <index>
insert <data> at beg
insert <data> at end
remove <index>
quit
The list: 
What would you like to do? insert 7 at beg
The list: 7 
What would you like to do? insert 1 before 0
The list: 7 1 
What would you like to do? insert 10 after 0
The list: 7 10 1 
What would you like to do? insert 3 at end
The list: 7 10 1 3 
What would you like to do? remove 2
The list: 7 10 3 
What would you like to do? remove 0
The list: 10 3 
What would you like to do? quit
 
Case 2:
Menu
insert <data> after <index>
insert <data> before <index>
insert <data> at beg
insert <data> at end
remove <index>
quit
The list: 
What would you like to do? insert 1 at beg
The list: 1 
What would you like to do? insert 3 after 2
No such index.
The list: 1 
What would you like to do? remove 1
No such index.
The list: 1 
What would you like to do? insert 6 after 0
The list: 1 6 
What would you like to do? remove 0
The list: 6 
What would you like to do? quit
```

## 3. Python program to check whether a singly linked list is a palindrome.

Problem Description
The program creates a linked list using data items input from the user and determines whether it is a palindrome.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variables head and last_node.
3. The variable head points to the first element in the linked list while last_node points to the last.
4. Define methods append and display inside the class LinkedList to append data and display the linked list respectively.
5. Define method get_prev_node which takes a reference node as argument and returns the node before it.
6. Define a function is_palindrome which returns True if the linked list passed to it is a palindrome.
7. The function is_palindrome iterates through the linked list from the start and the last node towards the middle to check if the list is a palindrome.
8. Create an instance of LinkedList, append data to it and determine whether it is a palindrome.

Program/Source Code
Here is the source code of a Python program to check whether a singly linked list is a palindrome.
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
 
 
def is_palindrome(llist):
    start = llist.head
    end = llist.last_node
    while (start != end and end.next != start):
        if start.data != end.data:
            return False
        start = start.next
        end = llist.get_prev_node(end)
    return True
 
 
a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
if is_palindrome(a_llist):
    print('The linked list is palindromic.')
else:
    print('The linked list is not palindromic.')
```    
Program Explanation
1. An instance of LinkedList is created.
2. The user is prompted to enter the data items for the list.
3. The function is_palindrome is called with the list as argument to determine whether it is a palindrome.
4. The result is then displayed.

```
Runtime Test Cases
Case 1:
Please enter the elements in the linked list: 7 8 1 8 7
The linked lists is palindromic.
 
Case 2:
Please enter the elements in the linked list: 1 2 3 3 2 1
The linked list is palindromic.
 
Case 3:
Please enter the elements in the linked list: 1 4 5 4 5 1
The linked list is not palindromic.
```


## 4.Python program to convert a given singly linked list to a circular list.

Problem Description
The program creates a singly linked list and converts it into a circular list.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class LinkedList with instance variables head and last_node.
3. The variable head points to the first element in the single linked list while last_node points to the last.
4. Define method append to append data items to the list.
5. Define function convert_to_circular which takes a singly linked list as argument.
6. The function convert_to_circular converts the list passed into a circular list by making the last node point to the first.
7. Define function print_last_node_points_to to display what the last node of the passed linked list points to.
8. Create an instance of LinkedList, append data to it and convert it to a circular list.

Program/Source Code
Here is the source code of a Python program to convert a singly linked list to a circular list. The program output is shown below.
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
 
 
def convert_to_circular(llist):
    if llist.last_node:
        llist.last_node.next = llist.head
 
 
def print_last_node_points_to(llist):
    last = llist.last_node
    if last is None:
        print('List is empty.')
        return
    if last.next is None:
        print('Last node points to None.')
    else:
        print('Last node points to element with data {}.'.format(last.next.data))
 
 
a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
print_last_node_points_to(a_llist)
 
print('Converting linked list to a circular linked list...')
convert_to_circular(a_llist)
 
print_last_node_points_to(a_llist)
```
Program Explanation
1. An instance of LinkedList is created.
2. The user is prompted to enter the data items for the list.
3. The singly linked list is converted to a circular list by passing the list to the function convert_to_circular.
4. The user is shown to what the last node of the list points to before and after the conversion by calling the function print_last_node_points_to.

```
Runtime Test Cases
Case 1:
Please enter the elements in the linked list: 7 2 3 40 1
Last node points to None.
Converting linked list to a circular linked list...
Last node points to element with data 7.
 
Case 2:
Please enter the elements in the linked list: 3
Last node points to None.
Converting linked list to a circular linked list...
Last node points to element with data 3.
 
Case 3:
Please enter the elements in the linked list: 1 2
Last node points to None.
Converting linked list to a circular linked list...
Last node points to element with data 1.
```

