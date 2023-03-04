
## 1. Python program to implement a binary heap.

Problem Description
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
