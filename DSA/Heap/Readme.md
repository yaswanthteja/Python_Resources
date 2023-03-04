
## 1. Python program to implement a binary heap.

## Problem Description
The program creates a binary max-heap and presents a menu to the user to perform various operations on it.

Problem Solution
1. Create a class BinaryHeap with an instance variable items set to an empty list. This empty list is used to store the binary heap.
2. Define methods size, parent, left, right, get, get_max, extract_max, max_heapify, swap and insert.
3. The method size returns the number of elements in the heap.
4. The method parent takes an index as argument and returns the index of the parent.
5. The method left takes an index as argument and returns the index of its left child.
6. The method right takes an index as argument and returns the index of its right child.
7. The method get takes an index as argument and returns the key at the index.
8. The method get_max returns the maximum element in the heap by returning the first element in the list items.
9. The method extract_max returns the the maximum element in the heap and removes it.
10. The method max_heapify takes an index as argument and modifies the heap structure at and below the node at this index to make it satisfy the heap property.
11. The method swap takes two indexes as arguments and swaps the corresponding elements in the heap.
12. The method insert takes a key as argument and adds that key to the heap.

Program/Source Code
Here is the source code of a Python program to implement a binary heap. The program output is shown below.
```
class BinaryHeap:
    def __init__(self):
        self.items = []
 
    def size(self):
        return len(self.items)
 
    def parent(self, i):
        return (i - 1)//2
 
    def left(self, i):
        return 2*i + 1
 
    def right(self, i):
        return 2*i + 2
 
    def get(self, i):
        return self.items[i]
 
    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]
 
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest
 
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= self.size() - 1 and self.get(l) > self.get(i)):
            largest = l
        else:
            largest = i
        if (r <= self.size() - 1 and self.get(r) > self.get(largest)):
            largest = r
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)
 
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
 
    def insert(self, key):
        index = self.size()
        self.items.append(key)
 
        while (index != 0):
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p
 
 
bheap = BinaryHeap()
 
print('Menu')
print('insert <data>')
print('max get')
print('max extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'max':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(bheap.get_max()))
        elif suboperation == 'extract':
            print('Maximum value removed: {}'.format(bheap.extract_max()))
 
    elif operation == 'quit':
        break
```
Program Explanation
1. Create an instance of BinaryHeap.
2. The user is presented with a menu to perform various operations on the heap.
3. The corresponding methods are called to perform each operation.



## Runtime Test Cases

```


Case 1:
Menu
insert <data>
max get
max extract
quit
What would you like to do? insert 5
What would you like to do? insert 3
What would you like to do? insert -3
What would you like to do? insert 10
What would you like to do? insert 8
What would you like to do? max get
Maximum value: 10
What would you like to do? max extract
Maximum value removed: 10
What would you like to do? max extract
Maximum value removed: 8
What would you like to do? max extract
Maximum value removed: 5
What would you like to do? max extract
Maximum value removed: 3
What would you like to do? max get
Maximum value: -3
What would you like to do? quit
 
Case 2:
Menu
insert <data>
max get
max extract
quit
What would you like to do? insert 3
What would you like to do? insert 11
What would you like to do? insert 5
What would you like to do? max extract
Maximum value removed: 11
What would you like to do? max get
Maximum value: 5
What would you like to do? max extract
Maximum value removed: 5
What would you like to do? insert 15
What would you like to do? max get
Maximum value: 15
What would you like to do? quit
```
## 2. Python program to implement a binomial heap.

Problem Description
The program creates a binomial min-heap and presents a menu to the user to perform various operations on it.

Problem Solution
1. Create a class BinomialTree with instance variables key, children and order. children is set to an empty list and order is set to 0 when an object is instantiated.
2. Define method add_at_end which takes a binomial tree of the same order as argument and adds it to the current tree, increasing its order by 1.
3. Create a class BinomialHeap with an instance variable trees set to an empty list. This list will contain the set of binomial trees.
4. Define methods get_min, extract_min, combine_roots, merge and insert.
5. The method get_min returns the minimum element in the heap by returning the key of the smallest root in the list trees.
6. The method merge takes a heap as argument and merges it with the current heap. It iterates through the sorted (by order of each tree) list of trees and merges any two trees with the same order. It also checks for the case for three consecutive trees of the same order and merges the last two trees.
7. The method combine_roots takes a heap as argument and combines the current heap’s list of trees with its list of trees and sorts them by order of each tree.
8. The method extract_min removes and returns the minimum element in the current heap. It does so by removing the tree with the smallest root from the current heap’s list of trees and creating a heap with the children of the smallest root as its list of trees. This new heap is then merged with the current heap.
9. The method insert takes a key as argument and adds a node with that key to the heap. It does so by creating an order 0 heap with that key and then merging it with the current heap.

Program/Source Code
Here is the source code of a Python program to implement a binomial heap. The program output is shown below.
```
class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
 
 
class BinomialHeap:
    def __init__(self):
        self.trees = []
 
    def extract_min(self):
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
 
        return smallest_node.key
 
    def get_min(self):
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least
 
    def combine_roots(self, h):
        self.trees.extend(h.trees)
        self.trees.sort(key=lambda tree: tree.order)
 
    def merge(self, h):
        self.combine_roots(h)
        if self.trees == []:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees) - 1
                    and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i + 1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i = i + 1
 
    def insert(self, key):
        g = BinomialHeap()
        g.trees.append(BinomialTree(key))
        self.merge(g)
 
 
bheap = BinomialHeap()
 
print('Menu')
print('insert <data>')
print('min get')
print('min extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'min':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Minimum value: {}'.format(bheap.get_min()))
        elif suboperation == 'extract':
            print('Minimum value removed: {}'.format(bheap.extract_min()))
 
    elif operation == 'quit':
        break
        
```
Program Explanation
1. Create an instance of BinomialHeap.
2. The user is presented with a menu to perform various operations on the heap.
3. The corresponding methods are called to perform each operation.


## Runtime Test Cases
```

Case 1:
Menu
insert <data>
min get
min extract
quit
What would you like to do? insert 3
What would you like to do? insert 7
What would you like to do? insert 1
What would you like to do? insert 4
What would you like to do? min get
Minimum value: 1
What would you like to do? min extract
Minimum value removed: 1
What would you like to do? min extract
Minimum value removed: 3
What would you like to do? min extract
Minimum value removed: 4
What would you like to do? min extract
Minimum value removed: 7
What would you like to do? min extract
Minimum value removed: None
What would you like to do? quit
 
Case 2:
Menu
insert <data>
min get
min extract
quit
What would you like to do? insert 10
What would you like to do? insert 12
What would you like to do? insert 5
What would you like to do? insert 6
What would you like to do? min get
Minimum value: 5
What would you like to do? insert 3
What would you like to do? min get
Minimum value: 3
What would you like to do? insert 8
What would you like to do? min extract
Minimum value removed: 3
What would you like to do? min extract
Minimum value removed: 5
What would you like to do? insert 1
What would you like to do? min extract
Minimum value removed: 1
What would you like to do? quit
```

## 3. Python program to implement a Fibonacci heap.

Problem Description
The program creates a Fibonacci min-heap and presents a menu to the user to perform various operations on it.

Problem Solution
1. Create a class FibonacciTree with instance variables key, children and order. children is set to an empty list and order is set to 0 when an object is instantiated.
2. Define method add_at_end which takes a Fibonacci tree of the same order as argument and adds it to the current tree, increasing its order by 1.
3. Create a class FibonacciHeap with instance variables trees, least and count. The variable trees is set to an empty list, least to None and count to 0 on instantiation. The list will contain the set of Fibonacci trees, least will point to the tree with the least element and count will contain the number of nodes in the heap.
4. Define methods get_min, extract_min, consolidate and insert.
5. The method get_min returns the minimum element in the heap by returning the key of the variable least.
6. The method extract_min removes and returns the minimum element in the current heap. It does so by removing the tree that least points to from the current heap’s list of trees and then appending the children of the removed node to the list of trees. The method consolidate is then called before returning the key of the least element.
7. The method consolidate combines the trees in the heap such that there is at most one tree of any order. It also sets the variable least of the heap to the tree with the smallest element.
8. The method insert takes a key as argument and adds a node with that key to the heap. It does so by creating an order 0 Fibonacci tree with that key and appending it to list of trees of the heap. It then updates count and, if required, least.
9. Define the function floor_log2 which takes a number as argument and returns the floor of its base 2 logarithm.

Program/Source Code
Here is the source code of a Python program to implement a Fibonacci heap. The program output is shown below.
```
import math
 
class FibonacciTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
 
 
class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0
 
    def insert(self, key):
        new_tree = FibonacciTree(key)
        self.trees.append(new_tree)
        if (self.least is None or key < self.least.key):
            self.least = new_tree
        self.count = self.count + 1
 
    def get_min(self):
        if self.least is None:
            return None
        return self.least.key
 
    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key
 
    def consolidate(self):
        aux = (floor_log2(self.count) + 1)*[None]
 
        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x
 
        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                    or k.key < self.least.key):
                    self.least = k
 
 
def floor_log2(x):
    return math.frexp(x)[1] - 1
 
 
fheap = FibonacciHeap()
 
print('Menu')
print('insert <data>')
print('min get')
print('min extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        fheap.insert(data)
    elif operation == 'min':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Minimum value: {}'.format(fheap.get_min()))
        elif suboperation == 'extract':
            print('Minimum value removed: {}'.format(fheap.extract_min()))
 
    elif operation == 'quit':
        break
```
Program Explanation
1. Create an instance of FibonacciHeap.
2. The user is presented with a menu to perform various operations on the heap.
3. The corresponding methods are called to perform each operation.


## Runtime Test Cases
```

Case 1:
Menu
insert <data>
min get
min extract
quit
What would you like to do? insert 3
What would you like to do? insert 2
What would you like to do? insert 7
What would you like to do? min get
Minimum value: 2
What would you like to do? min extract
Minimum value removed: 2
What would you like to do? min extract
Minimum value removed: 3
What would you like to do? min extract
Minimum value removed: 7
What would you like to do? min extract
Minimum value removed: None
What would you like to do? quit
 
Case 2:
Menu
insert <data>
min get
min extract
quit
What would you like to do? insert 1
What would you like to do? insert 2
What would you like to do? insert 3
What would you like to do? insert 4
What would you like to do? insert 0
What would you like to do? min extract
Minimum value removed: 0
What would you like to do? min extract
Minimum value removed: 1
What would you like to do? min extract
Minimum value removed: 2
What would you like to do? min extract
Minimum value removed: 3
What would you like to do? min extract
Minimum value removed: 4
What would you like to do? quit
```

## 4.  Python program to implement a d-ary heap.

Problem Description
The program creates a d-ary max-heap and presents a menu to the user to perform various operations on it.

Problem Solution
1. Create a class D_aryHeap with instance variables items set to an empty list and d. The list items is used to store the d-ary heap while d represents the number of children each node can have in the heap.
2. Define methods size, parent, child, get, get_max, extract_max, max_heapify, swap and insert.
3. The method size returns the number of elements in the heap.
4. The method parent takes an index as argument and returns the index of the parent.
5. The method child takes an index and position as arguments and returns the index of the child at that position from the left.
6. The method get takes an index as argument and returns the key at the index.
7. The method get_max returns the maximum element in the heap by returning the first element in the list items.
8. The method extract_max returns the the maximum element in the heap and removes it.
9. The method max_heapify takes an index as argument and modifies the heap structure at and below the node at this index to make it satisfy the heap property.
10. The method swap takes two indexes as arguments and swaps the corresponding elements in the heap.
11. The method insert takes a key as argument and adds that key to the heap.

Program/Source Code
Here is the source code of a Python program to implement a d-ary heap. The program output is shown below.
```
class D_aryHeap:
    def __init__(self, d):
        self.items = []
        self.d = d
 
    def size(self):
        return len(self.items)
 
    def parent(self, i):
        return (i - 1)//self.d
 
    def child(self, index, position):
        return index*self.d + (position + 1)
 
    def get(self, i):
        return self.items[i]
 
    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]
 
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest
 
    def max_heapify(self, i):
        largest = i
        for j in range(self.d):
            c = self.child(i, j)
            if (c < self.size() and self.get(c) > self.get(largest)):
                largest = c
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)
 
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
 
    def insert(self, key):
        index = self.size()
        self.items.append(key)
        while (index != 0):
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p
 
 
d = int(input('Enter the value of D: '));
dheap = D_aryHeap(d)
 
print('Menu (this assumes no duplicate keys)')
print('insert <data>')
print('max get')
print('max extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        dheap.insert(data)
    elif operation == 'max':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(dheap.get_max()))
        elif suboperation == 'extract':
            print('Maximum value removed: {}'.format(dheap.extract_max()))
 
    elif operation == 'quit':
        break
```
Program Explanation
1. The user is prompted to enter the value of the number of children for each node in the heap.
2. An instance of D_aryHeap is created.
3. The user is presented with a menu to perform various operations on the heap.
4. The corresponding methods are called to perform each operation.

```
Runtime Test Cases
Case 1:
Enter the value of D: 5
Menu (this assumes no duplicate keys)
insert <data>
max get
max extract
quit
What would you like to do? insert 3
What would you like to do? insert 4
What would you like to do? insert 11
What would you like to do? insert 7
What would you like to do? max get
Maximum value: 11
What would you like to do? max extract
Maximum value removed: 11
What would you like to do? max extract
Maximum value removed: 7
What would you like to do? max extract
Maximum value removed: 4
What would you like to do? max extract
Maximum value removed: 3
What would you like to do? max extract
Maximum value removed: None
What would you like to do? quit
 
Case 2:
Enter the value of D: 2
Menu (this assumes no duplicate keys)
insert <data>
max get
max extract
quit
What would you like to do? insert 1
What would you like to do? insert 3
What would you like to do? insert 2
What would you like to do? max extract
Maximum value removed: 3
What would you like to do? max extract
Maximum value removed: 2
What would you like to do? max extract
Maximum value removed: 1
What would you like to do? quit
```
## 5.Python program to implement a ternary heap.

Problem Description
The program creates a ternary max-heap and presents a menu to the user to perform various operations on it.

Problem Solution
1. Create a class TernaryHeap with an instance variable items set to an empty list. This empty list is used to store the ternary heap.
2. Define methods size, parent, left, mid, right, get, get_max, extract_max, max_heapify, swap and insert.
3. The method size returns the number of elements in the heap.
4. The method parent takes an index as argument and returns the index of the parent.
5. The method left takes an index as argument and returns the index of its left child.
6. The method mid takes an index as argument and returns the index of its middle child.
7. The method right takes an index as argument and returns the index of its right child.
8. The method get takes an index as argument and returns the key at the index.
9. The method get_max returns the maximum element in the heap by returning the first element in the list items.
10. The method extract_max returns the the maximum element in the heap and removes it.
11. The method max_heapify takes an index as argument and modifies the heap structure at and below the node at this index to make it satisfy the heap property.
12. The method swap takes two indexes as arguments and swaps the corresponding elements in the heap.
13. The method insert takes a key as argument and adds that key to the heap.

Program/Source Code
Here is the source code of a Python program to implement a ternary heap. The program output is shown below.
```
class TernaryHeap:
    def __init__(self):
        self.items = []
 
    def size(self):
        return len(self.items)
 
    def parent(self, i):
        return (i - 1)//3
 
    def left(self, i):
        return 3*i + 1
 
    def mid(self, i):
        return 3*i + 2
 
    def right(self, i):
        return 3*i + 3
 
    def get(self, i):
        return self.items[i]
 
    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]
 
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest
 
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        m = self.mid(i)
        if (l <= self.size() - 1 and self.get(l) > self.get(i)):
            largest = l
        else:
            largest = i
        if (m <= self.size() - 1 and self.get(m) > self.get(largest)):
            largest = m
        if (r <= self.size() - 1 and self.get(r) > self.get(largest)):
            largest = r
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)
 
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
 
    def insert(self, key):
        index = self.size()
        self.items.append(key)
 
        while (index != 0):
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p
 
 
theap = TernaryHeap()
 
print('Menu (this assumes no duplicate keys)')
print('insert <data>')
print('max get')
print('max extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        theap.insert(data)
    elif operation == 'max':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(theap.get_max()))
        elif suboperation == 'extract':
            print('Maximum value removed: {}'.format(theap.extract_max()))
 
    elif operation == 'quit':
        break
```
Program Explanation
1. Create an instance of TernaryHeap.
2. The user is presented with a menu to perform various operations on the heap.
3. The corresponding methods are called to perform each operation.

## Runtime Test Cases
```

Case 1:
Menu (this assumes no duplicate keys)
insert <data>
max get
max extract
quit
What would you like to do? insert 3
What would you like to do? insert 1
What would you like to do? insert 7
What would you like to do? max extract
Maximum value removed: 7
What would you like to do? max extract
Maximum value removed: 3
What would you like to do? max extract
Maximum value removed: 1
What would you like to do? max extract
Maximum value removed: None
What would you like to do? quit
 
Case 2:
Menu (this assumes no duplicate keys)
insert <data>
max get
max extract
quit
What would you like to do? insert 10
What would you like to do? insert 2
What would you like to do? max get
Maximum value: 10
What would you like to do? insert 15
What would you like to do? max extract
Maximum value removed: 15
What would you like to do? max extract
Maximum value removed: 10
What would you like to do? quit
```
