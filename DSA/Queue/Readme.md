

## Python program to implement a queue.

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


