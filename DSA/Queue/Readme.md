

## 1. Python program to implement a queue.

Problem Description
The program creates a queue and allows the user to perform enqueue and dequeue operations on it.

Problem Solution
1. Create a class Queue with instance variable items initialized to an empty list.
2. Define methods enqueue, dequeue and is_empty inside the class Queue.
3. The method enqueue appends data to items.
4. The method dequeue dequeues the first element in items.
5. The method is_empty returns True only if items is empty.
6. Create an instance of Queue and present a menu to the user to perform operations on the queue.

Program/Source Code
Here is the source code of a Python program to implement a queue. The program output is shown below.
```
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
 
 
q = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        q.enqueue(int(do[1]))
    elif operation == 'dequeue':
        if q.is_empty():
            print('Queue is empty.')
        else:
            print('Dequeued value: ', q.dequeue())
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Queue is created.
2. The user is presented with a menu to perform enqueue and dequeue operations on the queue.
3. The chosen operation is performed by calling the corresponding method of the queue.

```
Runtime Test Cases
Case 1:
enqueue <value>
dequeue
quit
What would you like to do? enqueue 3
enqueue <value>
dequeue
quit
What would you like to do? enqueue 1
enqueue <value>
dequeue
quit
What would you like to do? enqueue 0
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Dequeued value:  3
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Dequeued value:  1
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Dequeued value:  0
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Queue is empty.
enqueue <value>
dequeue
quit
What would you like to do? quit
 
Case 2:
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Queue is empty.
enqueue <value>
dequeue
quit
What would you like to do? enqueue 7
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Dequeued value:  7
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Queue is empty.
enqueue <value>
dequeue
quit
What would you like to do? quit
```

## 2. Python program to implement a dequeue.

Problem Description
The program creates a dequeue and allows the user to perform append and pop operations on it from both sides.

Problem Solution
1. Create a class Dequeue with instance variable items initialized to an empty list.
2. Define methods append, append_left, pop, pop_left and is_empty inside the class Dequeue.
3. The method append appends data to items from the right.
4. The method append_left appends data to items from the left.
5. The method pop pops from the right from items.
6. The method pop_left pops from the left from items.
7. The method is_empty returns True only if items is empty.

Program/Source Code
Here is the source code of a Python program to implement a dequeue. The program output is shown below.
```
class Dequeue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def append(self, data):
        self.items.append(data)
 
    def append_left(self, data):
        self.items.insert(0, data)
 
    def pop(self):
        return self.items.pop()
 
    def pop_left(self):
        return self.items.pop(0)
 
 
q = Dequeue()
print('Menu')
print('append <value>')
print('appendleft <value>')
print('pop')
print('popleft')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'append':
        q.append(int(do[1]))
    elif operation == 'appendleft':
        q.append_left(int(do[1]))
    elif operation == 'pop':
        if q.is_empty():
            print('Dequeue is empty.')
        else:
            print('Popped value from right: ', q.pop())
    elif operation == 'popleft':
        if q.is_empty():
            print('Dequeue is empty.')
        else:
            print('Popped value from left: ', q.pop_left())
    elif operation == 'quit':
        break
  ```
Program Explanation
1. An instance of Dequeue is created.
2. The user is presented with a menu to perform various operations on the dequeue.
3. The chosen operation is performed by calling the corresponding method of the dequeue.


```
Runtime Test Cases
Case 1:
Menu
append <value>
appendleft <value>
pop
popleft
quit
What would you like to do? append 3
What would you like to do? append 4
What would you like to do? appendleft 2
What would you like to do? appendleft 1
What would you like to do? pop
Popped value from right:  4
What would you like to do? popleft
Popped value from left:  1
What would you like to do? pop
Popped value from right:  3
What would you like to do? popleft
Popped value from left:  2
What would you like to do? pop
Dequeue is empty.
What would you like to do? quit
 
Case 2:
Menu
append <value>
appendleft <value>
pop
popleft
quit
What would you like to do? append 1
What would you like to do? append 2
What would you like to do? pop
Popped value from right:  2
What would you like to do? pop
Popped value from right:  1
What would you like to do? appendleft 1
What would you like to do? appendleft 2
What would you like to do? pop
Popped value from right:  1
What would you like to do? pop
Popped value from right:  2
What would you like to do? append 1
What would you like to do? append 2
What would you like to do? popleft
Popped value from left:  1
What would you like to do? popleft
Popped value from left:  2
What would you like to do? quit

```

## 3.Python program to implement a queue using two stacks.

Problem Description
The program creates a queue using stacks and allows the user to perform enqueue and dequeue operations on it.

Problem Solution
1. Create a class Node with instance variables data and next.
2. Create a class Stack with instance variable items initialized to an empty list.
3. Define methods push, pop and is_empty inside the class Stack.
4. The method push appends data to items.
5. The method pop pops the first element in items.
6. The method is_empty returns True only if items is empty.
7. Create a class Queue with instance variables inbox and outbox, both initialized to an empty stack.
8. Define methods enqueue, dequeue and is_empty inside the class Queue.
9. The method enqueue pushes data to the stack inbox.
10. The method dequeue pops from the stack outbox if it is not empty. If it is empty, then all the elements from inbox are popped and pushed to outbox before popping from outbox.
11. The method is_empty returns True only if both the stacks inbox and outbox are empty.
12. Create an instance of Queue and present a menu to the user to perform operations on the queue.

Program/Source Code
Here is the source code of a Python program to implement a queue using two stacks. The program output is shown below.
```
class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
 
    def is_empty(self):
        return (self.inbox.is_empty() and self.outbox.is_empty())
 
    def enqueue(self, data):
        self.inbox.push(data)
 
    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                popped = self.inbox.pop()
                self.outbox.push(popped)
        return self.outbox.pop()
 
 
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
a_queue = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        if a_queue.is_empty():
            print('Queue is empty.')
        else:
            dequeued = a_queue.dequeue()
            print('Dequeued element: ', int(dequeued))
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Queue is created.
2. The user is presented with a menu to perform enqueue and dequeue operations on the queue.
3. The chosen operation is performed by calling the corresponding method.

```
Runtime Test Cases
Case 1:
enqueue <value>
dequeue
quit
What would you like to do? enqueue 7
enqueue <value>
dequeue
quit
What would you like to do? enqueue 8
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Dequeued element:  7
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Dequeued element:  8
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Queue is empty.
enqueue <value>
dequeue
quit
What would you like to do? quit
 
Case 2:
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Queue is empty.
enqueue <value>
dequeue
quit
What would you like to do? enqueue 1
enqueue <value>
dequeue
quit
What would you like to do? enqueue 2
enqueue <value>
dequeue
quit
What would you like to do? dequeue
Dequeued element:  1
enqueue <value>
dequeue
quit
What would you like to do? quit
```


