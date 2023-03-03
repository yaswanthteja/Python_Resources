
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

