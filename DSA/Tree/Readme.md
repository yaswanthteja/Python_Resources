
## 1. Python program to implement a binomial tree.

Problem Description
The program creates binomial trees and presents a menu to the user to perform operations on these trees.

Problem Solution
1. Create a class BinomialTree with instance variables key, children and order. children is set to an empty list and order is set to 0 when an object is instantiated.
2. Define method add_at_end which takes a binomial tree of the same order as argument and adds it to the current tree, increasing its order by 1.

Program/Source Code
Here is the source code of a Python program to implement a binomial tree. The program output is shown below.
```
class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
 
 
trees = []
 
print('Menu')
print('create <key>')
print('combine <index1> <index2>')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'create':
        key = int(do[1])
        btree = BinomialTree(key)
        trees.append(btree)
        print('Binomial tree created.')
    elif operation == 'combine':
        index1 = int(do[1])
        index2 = int(do[2])
        if trees[index1].order == trees[index2].order:
            trees[index1].add_at_end(trees[index2])
            del trees[index2]
            print('Binomial trees combined.')
        else:
            print('Orders of the trees need to be the same.')
 
    elif operation == 'quit':
        break
 
    print('{:>8}{:>12}{:>8}'.format('Index', 'Root key', 'Order'))
    for index, t in enumerate(trees):
        print('{:8d}{:12d}{:8d}'.format(index, t.key, t.order))
 ```
Program Explanation
1. An empty list is created to store the binomial trees.
2. The user is presented with a menu to create and combine two binomial trees.
3. Only trees of the same order k are allowed to combine to form a tree of order k + 1.
4. The corresponding methods are called to perform each operation.

## Runtime Test Cases
```

Case 1:
create <key>
combine <index1> <index2>
quit
What would you like to do? create 7
Binomial tree created.
   Index    Root key   Order
       0           7       0
What would you like to do? create 3
Binomial tree created.
   Index    Root key   Order
       0           7       0
       1           3       0
What would you like to do? create 4
Binomial tree created.
   Index    Root key   Order
       0           7       0
       1           3       0
       2           4       0
What would you like to do? create 1
Binomial tree created.
   Index    Root key   Order
       0           7       0
       1           3       0
       2           4       0
       3           1       0
What would you like to do? combine 0 1
Binomial trees combined.
   Index    Root key   Order
       0           7       1
       1           4       0
       2           1       0
What would you like to do? combine 1 2
Binomial trees combined.
   Index    Root key   Order
       0           7       1
       1           4       1
What would you like to do? combine 0 1
Binomial trees combined.
   Index    Root key   Order
       0           7       2
What would you like to do? quit
 
Case 2:
Menu
create <key>
combine <index1> <index2>
quit
What would you like to do? create 2
Binomial tree created.
   Index    Root key   Order
       0           2       0
What would you like to do? create 3
Binomial tree created.
   Index    Root key   Order
       0           2       0
       1           3       0
What would you like to do? create 1
Binomial tree created.
   Index    Root key   Order
       0           2       0
       1           3       0
       2           1       0
What would you like to do? combine 2 0
Binomial trees combined.
   Index    Root key   Order
       0           3       0
       1           1       1
What would you like to do? quit
```
## 2.  Python program to construct a tree and perform insertion, deletion and display operations.

Problem Description
The program creates a tree and presents a menu to the user to perform insertion, deletion and display operations.

Problem Solution
1. Create a class Tree with instance variables key and children.
2. Define methods set_root, add, remove, bfs_display and search.
3. The method set_root takes a key as argument and sets the instance variable key equal to it.
4. The method add appends a node to the list children.
5. The method search returns a node with a specified key.
6. The method remove removes the current node from the tree.
7. The method bfs_display displays the BFS traversal of the tree.

Program/Source Code
Here is the source code of a Python program to construct a tree and perform insertion, deletion and display operations. The program output is shown below.
```
class Tree:
    def __init__(self, data=None, parent=None):
        self.key = data
        self.children = []
        self.parent = parent
 
    def set_root(self, data):
        self.key = data
 
    def add(self, node):
        self.children.append(node)
 
    def search(self, key):
        if self.key == key:
            return self
        for child in self.children:
            temp = child.search(key)
            if temp is not None:
                return temp
        return None
 
    def remove(self):
        parent = self.parent
        index = parent.children.index(self)
        parent.children.remove(self)
        for child in reversed(self.children):
            parent.children.insert(index, child)
            child.parent = parent
 
    def bfs_display(self):
        queue = [self]
        while queue != []:
            popped = queue.pop(0)
            for child in popped.children:
                queue.append(child)
            print(popped.key, end=' ')
 
 
tree = None
 
print('Menu (this assumes no duplicate keys)')
print('add <data> at root')
print('add <data> below <data>')
print('remove <data>')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'add':
        data = int(do[1])
        new_node = Tree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            tree = new_node
        elif suboperation == 'below':
            position = do[3].strip().lower()
            key = int(position)
            ref_node = None
            if tree is not None:
                ref_node = tree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            new_node.parent = ref_node
            ref_node.add(new_node)
 
    elif operation == 'remove':
        data = int(do[1])
        to_remove = tree.search(data)
        if tree == to_remove:
            if tree.children == []:
                tree = None
            else:
                leaf = tree.children[0]
                while leaf.children != []:
                    leaf = leaf.children[0]
                leaf.parent.children.remove(leaf)
                leaf.parent = None
                leaf.children = tree.children
                tree = leaf
        else:
            to_remove.remove()
 
    elif operation == 'display':
        if tree is not None:
            print('BFS traversal display: ', end='')
            tree.bfs_display()
            print()
        else:
            print('Tree is empty.')
 
    elif operation == 'quit':
        break
```
Program Explanation
1. A variable is created to store the binary tree.
2. The user is presented with a menu to perform operations on the tree.
3. The corresponding methods are called to perform each operation.
4. If the node to be removed is the root node, the removal is carried out by finding a leaf node and replacing the root with it. If the node to be removed is not the root node then the remove method is called on the node.

## Runtime Test Cases

```

Case 1:
Menu (this assumes no duplicate keys)
add <data> at root
add <data> below <data>
remove <data>
display
quit
What would you like to do? add 1 at root
What would you like to do? add 2 below 1
What would you like to do? add 3 below 1
What would you like to do? add 4 below 2
What would you like to do? add 5 below 2
What would you like to do? display
BFS traversal display: 1 2 3 4 5 
What would you like to do? remove 1
What would you like to do? display
BFS traversal display: 4 2 3 5 
What would you like to do? remove 5
What would you like to do? display
BFS traversal display: 4 2 3 
What would you like to do? remove 4
What would you like to do? display
BFS traversal display: 2 3 
What would you like to do? remove 3
What would you like to do? remove 2
What would you like to do? display
Tree is empty.
What would you like to do? quit
 
Case 2:
Menu (this assumes no duplicate keys)
add <data> at root
add <data> below <data>
remove <data>
display
quit
What would you like to do? add 5 at root
What would you like to do? add 7 below 5
What would you like to do? add 9 below 7
What would you like to do? add 11 below 9
What would you like to do? add 12 below 7
What would you like to do? display
BFS traversal display: 5 7 9 12 11 
What would you like to do? remove 9
What would you like to do? display
BFS traversal display: 5 7 11 12 
What would you like to do? remove 12
What would you like to do? display
BFS traversal display: 5 7 11 
What would you like to do? remove 7
What would you like to do? display
BFS traversal display: 5 11 
What would you like to do? remove 5
What would you like to do? display
BFS traversal display: 11 
What would you like to do? quit

```
## 3.Python program to find the number of nodes in a binary tree.

Problem Description
The program creates a binary tree and counts the number of nodes in the tree.

Problem Solution
1. Create a class BinaryTree with instance variables key, left and right.
2. Define methods set_root, insert_left, insert_right, inorder and search.
3. The method set_root takes a key as argument and sets the variable key equal to it.
4. The methods insert_left and insert_right insert a node as the left and right child respectively.
5. The method inorder displays the inorder traversal.
6. The method search returns a node with a specified key.
7. Define the function count_nodes which takes a binary tree as argument.
8. The recursive function count_nodes returns the number of nodes in the binary tree.

Program/Source Code
Here is the source code of a Python program to count the number of nodes in a binary tree. The program output is shown below.
```
class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
 
    def set_root(self, key):
        self.key = key
 
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()
 
    def insert_left(self, new_node):
        self.left = new_node
 
    def insert_right(self, new_node):
        self.right = new_node
 
    def search(self, key):
        if self.key == key:
            return self
        if self.left is not None:
            temp =  self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(key)
            return temp
        return None
 
 
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
 
 
btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('count')
print('quit')
 
while True:
    print('inorder traversal of binary tree: ', end='')
    if btree is not None:
        btree.inorder()
    print()
 
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        new_node = BinaryTree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
                btree = new_node
        else:
            position = do[4].strip().lower()
            key = int(position)
            ref_node = None
            if btree is not None:
                ref_node = btree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            if suboperation == 'left':
                ref_node.insert_left(new_node)
            elif suboperation == 'right':
                ref_node.insert_right(new_node)
 
    elif operation == 'count':
        print('Number of nodes in tree: {}'.format(count_nodes(btree)))
 
    elif operation == 'quit':
        break
 ```
Program Explanation
1. A variable is created to store the binary tree.
2. The user is presented with a menu to perform operations on the tree.
3. The corresponding methods are called to perform each operation.
4. The function count_nodes is called to count the number of nodes in the binary tree.

## Runtime Test Cases
```

Case 1:
Menu (this assumes no duplicate keys)
insert <data> at root
insert <data> left of <data>
insert <data> right of <data>
count
quit
inorder traversal of binary tree: 
What would you like to do? insert 1 at root
inorder traversal of binary tree: 1 
What would you like to do? insert 2 left of 1
inorder traversal of binary tree: 2 1 
What would you like to do? insert 3 right of 1
inorder traversal of binary tree: 2 1 3 
What would you like to do? insert 4 right of 2
inorder traversal of binary tree: 2 4 1 3 
What would you like to do? count
Number of nodes in tree: 4
inorder traversal of binary tree: 2 4 1 3 
What would you like to do? quit
 
Case 2:
Menu (this assumes no duplicate keys)
insert <data> at root
insert <data> left of <data>
insert <data> right of <data>
count
quit
inorder traversal of binary tree: 
What would you like to do? count
Number of nodes in tree: 0
inorder traversal of binary tree: 
What would you like to do? insert 1 at root
inorder traversal of binary tree: 1 
What would you like to do? count
Number of nodes in tree: 1
inorder traversal of binary tree: 1 
What would you like to do? insert 2 right of 1
inorder traversal of binary tree: 1 2 
What would you like to do? count
Number of nodes in tree: 2
inorder traversal of binary tree: 1 2 
What would you like to do? quit

```
## 4.Python program to display the nodes of a tree using BFS traversal.

Problem Description
The program creates a tree and presents a menu to the user to perform various operations including printing its BFS traversal.

Problem Solution
1. Create a class Tree with instance variables key and children.
2. Define methods set_root, add, bfs and search.
3. The method set_root takes a key as argument and sets the instance variable key equal to it.
4. The method add appends a node to the list children.
5. The method search returns a node with a specified key.
6. The method bfs prints the BFS traversal of the tree. It uses a queue to do the traversal.

Program/Source Code
Here is the source code of a Python program to display the nodes of a tree using BFS traversal. The program output is shown below.
```
class Tree:
    def __init__(self, data=None):
        self.key = data
        self.children = []
 
    def set_root(self, data):
        self.key = data
 
    def add(self, node):
        self.children.append(node)
 
    def search(self, key):
        if self.key == key:
            return self
        for child in self.children:
            temp = child.search(key)
            if temp is not None:
                return temp
        return None
 
    def bfs(self):
        queue = [self]
        while queue != []:
            popped = queue.pop(0)
            for child in popped.children:
                queue.append(child)
            print(popped.key, end=' ')
 
 
tree = None
 
print('Menu (this assumes no duplicate keys)')
print('add <data> at root')
print('add <data> below <data>')
print('bfs')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'add':
        data = int(do[1])
        new_node = Tree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            tree = new_node
        elif suboperation == 'below':
            position = do[3].strip().lower()
            key = int(position)
            ref_node = None
            if tree is not None:
                ref_node = tree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            ref_node.add(new_node)
 
    elif operation == 'bfs':
        if tree is None:
            print('Tree is empty.')
        else:
            print('BFS traversal: ', end='')
            tree.bfs()
            print()
 
    elif operation == 'quit':
        break
    
```
Program Explanation
1. A variable is created to store the binary tree.
2. The user is presented with a menu to perform operations on the tree.
3. The corresponding methods are called to perform each operation.
4. The method bfs is called on the tree to print its breadth-first traversal.

## Runtime Test Cases
```

Case 1:
Menu (this assumes no duplicate keys)
add <data> at root
add <data> below <data>
bfs
quit
What would you like to do? add 1 at root
What would you like to do? add 2 below 1
What would you like to do? bfs
BFS traversal: 1 2 
What would you like to do? add 3 below 1
What would you like to do? add 10 below 2
What would you like to do? add 12 below 2
What would you like to do? add 14 below 3
What would you like to do? add 7 below 14
What would you like to do? bfs
BFS traversal: 1 2 3 10 12 14 7 
What would you like to do? quit
 
Case 2:
Menu (this assumes no duplicate keys)
add <data> at root
add <data> below <data>
bfs
quit
What would you like to do? add 5 at root
What would you like to do? add 7 below 5
What would you like to do? add 8 below 5
What would you like to do? add 4 below 7
What would you like to do? add 3 below 7
What would you like to do? add 1 below 8
What would you like to do? add 2 below 1
What would you like to do? bfs
BFS traversal: 5 7 8 4 3 1 2 
What would you like to do? quit

```


## 5. Python program to find the Nth node in the in-order traversal of a binary tree.

Problem Description
The program creates a binary tree and presents a menu to the user to perform operations on the tree including printing the Nth term in its in-order traversal.

Problem Solution
1. Create a class BinaryTree with instance variables key, left and right.
2. Define methods set_root, insert_left, insert_right, inorder_nth, inorder_nth_helper and search.
3. The method set_root takes a key as argument and sets the variable key equal to it.
4. The methods insert_left and insert_right insert a node as the left and right child respectively.
5. The method search returns a node with a specified key.
6. The method inorder_nth displays the nth element in the in-order traversal of the tree. It calls the recursive method inorder_nth_helper.

Program/Source Code
Here is the source code of a Python program to find the Nth node in the in-order traversal of a binary tree. The program output is shown below.
```
class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
 
    def set_root(self, key):
        self.key = key
 
    def inorder_nth(self, n):
        return self.inorder_nth_helper(n, [])
 
    def inorder_nth_helper(self, n, inord):
        if self.left is not None:
            temp = self.left.inorder_nth_helper(n, inord)
            if temp is not None:
                return temp
        inord.append(self)
        if n == len(inord):
            return self
        if self.right is not None:
            temp = self.right.inorder_nth_helper(n, inord)
            if temp is not None:
                return temp
 
    def insert_left(self, new_node):
        self.left = new_node
 
    def insert_right(self, new_node):
        self.right = new_node
 
    def search(self, key):
        if self.key == key:
            return self
        if self.left is not None:
            temp =  self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(key)
            return temp
        return None
 
 
btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('inorder <index>')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        new_node = BinaryTree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
                btree = new_node
        else:
            position = do[4].strip().lower()
            key = int(position)
            ref_node = None
            if btree is not None:
                ref_node = btree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            if suboperation == 'left':
                ref_node.insert_left(new_node)
            elif suboperation == 'right':
                ref_node.insert_right(new_node)
 
    elif operation == 'inorder':
        if btree is not None:
            index = int(do[1].strip().lower())
            node = btree.inorder_nth(index)
            if node is not None:
                print('nth term of inorder traversal: {}'.format(node.key))
            else:
                print('index exceeds maximum possible index.')
        else:
            print('Tree is empty.')
 
    elif operation == 'quit':
        break
```
Program Explanation
1. A variable is created to store the binary tree.
2. The user is presented with a menu to perform operations on the binary tree.
3. The corresponding methods are called to perform each operation.
4. The method inorder_nth is called to display the nth element in the in-order traversal of the tree.


## Runtime Test Cases

```

Case 1:
Menu (this assumes no duplicate keys)
insert <data> at root
insert <data> left of <data>
insert <data> right of <data>
inorder <index>
quit
What would you like to do? insert 1 at root
What would you like to do? insert 2 left of 1
What would you like to do? insert 3 right of 1
What would you like to do? inorder 1
nth term of inorder traversal: 2
What would you like to do? inorder 2
nth term of inorder traversal: 1
What would you like to do? inorder 3
nth term of inorder traversal: 3
What would you like to do? inorder 4
index exceeds maximum possible index.
What would you like to do? quit
 
Case 2:
Menu (this assumes no duplicate keys)
insert <data> at root
insert <data> left of <data>
insert <data> right of <data>
inorder <index>
quit
What would you like to do? insert 1 at root
What would you like to do? insert 3 left of 1
What would you like to do? insert 7 right of 1
What would you like to do? insert 5 right of 3
What would you like to do? insert 6 left of 5
What would you like to do? inorder 1
nth term of inorder traversal: 3
What would you like to do? inorder 2
nth term of inorder traversal: 6
What would you like to do? inorder 3
nth term of inorder traversal: 5
What would you like to do? inorder 4
nth term of inorder traversal: 1
What would you like to do? inorder 5
nth term of inorder traversal: 7
What would you like to do? inorder 6
index exceeds maximum possible index.
What would you like to do? quit
```

## 6. Python program to perform depth-first search on a binary tree using recursion.

Problem Description
The program creates a binary tree and presents a menu to the user to perform operations on the tree including depth-first search.

Problem Solution
1. Create a class BinaryTree with instance variables key, left and right.
2. Define methods set_root, insert_left, insert_right, depth_first and search.
3. The method set_root takes a key as argument and sets the variable key equal to it.
4. The methods insert_left and insert_right insert a node as the left and right child respectively.
5. The method depth_first displays a depth first traversal of the tree.
6. The method search returns a node with a specified key.

Program/Source Code
Here is the source code of a Python program to perform depth-first search on a binary tree using recursion. The program output is shown below.
```
class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
 
    def set_root(self, key):
        self.key = key
 
    def insert_left(self, new_node):
        self.left = new_node
 
    def insert_right(self, new_node):
        self.right = new_node
 
    def search(self, key):
        if self.key == key:
            return self
        if self.left is not None:
            temp =  self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(key)
            return temp
        return None
 
    def depth_first(self):
        print('entering {}...'.format(self.key))
        if self.left is not None:
            self.left.depth_first()
        print('at {}...'.format(self.key))
        if self.right is not None:
            self.right.depth_first()
        print('leaving {}...'.format(self.key))
 
 
btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('dfs')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        new_node = BinaryTree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
                btree = new_node
        else:
            position = do[4].strip().lower()
            key = int(position)
            ref_node = None
            if btree is not None:
                ref_node = btree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            if suboperation == 'left':
                ref_node.insert_left(new_node)
            elif suboperation == 'right':
                ref_node.insert_right(new_node)
 
    elif operation == 'dfs':
        print('depth-first search traversal:')
        if btree is not None:
            btree.depth_first()
        print()
 
    elif operation == 'quit':
        break
```
Program Explanation
1. A variable is created to store the binary tree.
2. The user is presented with a menu to perform operations on the tree.
3. The corresponding methods are called to perform each operation.
4. The method depth_first is called to display a DFS traversal of the tree.


## Runtime Test Cases
```

Case 1:
Menu (this assumes no duplicate keys)
insert <data> at root
insert <data> left of <data>
insert <data> right of <data>
dfs
quit
What would you like to do? insert 1 at root
What would you like to do? insert 2 left of 1
What would you like to do? insert 3 right of 1
What would you like to do? insert 4 left of 2
What would you like to do? insert 5 right of 2
What would you like to do? insert 6 left of 5
What would you like to do? insert 7 right of 5
What would you like to do? dfs
depth-first search traversal:
entering 1...
entering 2...
entering 4...
at 4...
leaving 4...
at 2...
entering 5...
entering 6...
at 6...
leaving 6...
at 5...
entering 7...
at 7...
leaving 7...
leaving 5...
leaving 2...
at 1...
entering 3...
at 3...
leaving 3...
leaving 1...
 
What would you like to do? quit
 
Case 2:
Menu (this assumes no duplicate keys)
insert <data> at root
insert <data> left of <data>
insert <data> right of <data>
dfs
quit
What would you like to do? insert 3 at root
What would you like to do? insert 4 left of 3
What would you like to do? insert 5 right of 3
What would you like to do? insert 6 left of 4
What would you like to do? dfs
depth-first search traversal:
entering 3...
entering 4...
entering 6...
at 6...
leaving 6...
at 4...
leaving 4...
at 3...
entering 5...
at 5...
leaving 5...
leaving 3...
 
What would you like to do? quit
```
