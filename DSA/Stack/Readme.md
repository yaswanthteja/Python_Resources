


## 1.Python program to implement a stack.

Problem Description
The program creates a stack and allows the user to perform push and pop operations on it.

Problem Solution
1. Create a class Stack with instance variable items initialized to an empty list.
2. Define methods push, pop and is_empty inside the class Stack.
3. The method push appends data to items.
4. The method pop pops the first element in items.
5. The method is_empty returns True only if items is empty.
6. Create an instance of Stack and present a menu to the user to perform operations on the stack.

Program/Source Code
Here is the source code of a Python program to implement a stack. The program output is shown below.
```
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
 ```
Program Explanation
1. An instance of Stack is created.
2. The user is presented with a menu to perform push and pop operations on the stack.
3. The chosen operation is performed by calling the corresponding method of the stack.

## Runtime Test Cases
```
Case 1:
push <value>
pop
quit
What would you like to do? push 3
push <value>
pop
quit
What would you like to do? push 5
push <value>
pop
quit
What would you like to do? pop
Popped value:  5
push <value>
pop
quit
What would you like to do? pop
Popped value:  3
push <value>
pop
quit
What would you like to do? pop
Stack is empty.
push <value>
pop
quit
What would you like to do? quit
 
Case 2:
push <value>
pop
quit
What would you like to do? pop
Stack is empty.
push <value>
pop
quit
What would you like to do? push 1
push <value>
pop
quit
What would you like to do? pop
Popped value:  1
push <value>
pop
quit
What would you like to do? quit
```
## 2. Python program to implement a stack using a single queue.

Problem Description
The program creates a stack using a single queue and allows the user to perform push and pop operations on it.

Problem Solution
1. Create a class Queue.
2. Define methods enqueue, dequeue, is_empty and get_size inside the class Queue.
3. Create a class Stack with instance variable q initialized to an empty queue.
4. Pushing is done by enqueuing data to the queue.
5. To pop, the queue is dequeued and enqueued with the dequeued element n – 1 times where n is the size of the queue. This causes the the last element added to the queue to reach the rear of the queue. The queue is dequeued one more time to get the item to be returned.
6. The method is_empty returns True iff the queue is empty.

Program/Source Code
Here is the source code of a Python program to implement a stack using a single queue. The program output is shown below.
```
class Stack:
    def __init__(self):
        self.q = Queue()
 
    def is_empty(self):
        return self.q.is_empty()
 
    def push(self, data):
        self.q.enqueue(data)
 
    def pop(self):
        for _ in range(self.q.get_size() - 1):
            dequeued = self.q.dequeue()
            self.q.enqueue(dequeued)
        return self.q.dequeue()
 
 
class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.size += 1
        self.items.append(data)
 
    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)
 
    def get_size(self):
        return self.size
 
 
s = Stack()
 
print('Menu')
print('push <value>')
print('pop')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
  ```
Program Explanation
1. An instance of Stack is created.
2. The user is presented with a menu to perform push and pop operations on the stack.
3. The chosen operation is performed by calling the corresponding method of the stack.

## Runtime Test Cases
```
Case 1:
Menu
push <value>
pop
quit
What would you like to do? push 3
What would you like to do? push 5
What would you like to do? pop
Popped value:  5
What would you like to do? pop
Popped value:  3
What would you like to do? pop
Stack is empty.
 
Case 2:
Menu
push <value>
pop
quit
What would you like to do? push 1
What would you like to do? push 2
What would you like to do? push 3
What would you like to do? push 4
What would you like to do? pop
Popped value:  4
What would you like to do? pop
Popped value:  3
What would you like to do? pop
Popped value:  2
What would you like to do? pop
Popped value:  1
What would you like to do? pop
Stack is empty.
What would you like to do? quit
```


## 3.  Python program to implement a stack using two queues.

Problem Description
The program creates a stack using two queues and allows the user to perform push and pop operations on it.

Problem Solution
1. Create a class Queue with instance variable items initialized to an empty list.
2. Define methods enqueue, dequeue and is_empty inside the class Queue.
3. The method enqueue appends data to items.
4. The method dequeue dequeues the first element in items.
5. The method is_empty returns True only if items is empty.
6. Create a class Stack with instance variable queue1 and queue2 initialized to empty queues.
7. Define methods push, pop and is_empty inside the class Stack.
8. The method push takes an argument and enqueues it in queue1. Then every element of queue2 is dequeued and enqueued in queue1. The names of queue1 and queue2 are then switched.
9. The method pop dequeues from queue2 and returns the dequeued value.
10. The method is_empty returns True only if queue2 is empty.

Program/Source Code
Here is the source code of a Python program to implement a stack using two queues. The program output is shown below.
```
class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
 
    def is_empty(self):
        return self.queue2.is_empty()
 
    def push(self, data):
        self.queue1.enqueue(data)
        while not self.queue2.is_empty():
            x = self.queue2.dequeue()
            self.queue1.enqueue(x)
        self.queue1, self.queue2 = self.queue2, self.queue1
 
    def pop(self):
        return self.queue2.dequeue()
 
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
 
 
s = Stack()
 
print('Menu')
print('push <value>')
print('pop')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
```
Program Explanation
1. An instance of Stack is created.
2. The user is presented with a menu to perform push and pop operations on the stack.
3. The chosen operation is performed by calling the corresponding method of the stack.


## Runtime Test Cases
```

Case 1:
Menu
push <value>
pop
quit
What would you like to do? pop
Stack is empty.
What would you like to do? push 3
What would you like to do? push 4
What would you like to do? pop
Popped value:  4
What would you like to do? pop
Popped value:  3
What would you like to do? pop
Stack is empty.
What would you like to do? push 1
What would you like to do? push 2
What would you like to do? pop
Popped value:  2
What would you like to do? quit
 
Case 2:
Menu
push <value>
pop
quit
What would you like to do? push 1
What would you like to do? push 2
What would you like to do? push 5
What would you like to do? push 0
What would you like to do? pop
Popped value:  0
What would you like to do? pop
Popped value:  5
What would you like to do? pop
Popped value:  2
What would you like to do? pop
Popped value:  1
What would you like to do? pop
Stack is empty.
What would you like to do? quit
```

## 4.  Python program to reverse a stack using recursion.

Problem Description
The program creates a stack and allows the user to perform push and pop operations on it.

Problem Solution
1. Create a class Stack with instance variable items initialized to an empty list.
2. Define methods push, pop, is_empty and display inside the class Stack.
3. The method push appends data to items.
4. The method pop pops the first element in items.
5. The method is_empty returns True only if items is empty.
6. The method display prints the elements of the stack from top to bottom.
7. Define function insert_at_bottom which takes a stack and a data item as arguments.
8. The function insert_at_bottom adds the data item to the bottom of the stack using recursion.
9. Define function reverse_stack which takes a stack as argument.
10. The function reverse_stack reverses the stack using recursion.
11. Create an instance of Stack, push data to it and reverse the stack.

Program/Source Code
Here is the source code of a Python program to reverse a stack. The program output is shown below.
```
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
    def display(self):
        for data in reversed(self.items):
            print(data)
 
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)
 
 
def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)
 
 
s = Stack()
data_list = input('Please enter the elements to push: ').split()
for data in data_list:
    s.push(int(data))
 
print('The stack:')
s.display()
reverse_stack(s)
print('After reversing:')
s.display()
```
Program Explanation
1. An instance of Stack is created.
2. The user is prompted to enter data items to push to the stack.
3. The stack is displayed.
4. The stack is reversed by passing it to the function reverse_stack.
5. The stack is displayed again.

## Runtime Test Cases
```
Case 1:
Please enter the elements to push: 7 3 1 5
The stack:
5
1
3
7
After reversing:
7
3
1
5
 
Case 2:
Please enter the elements to push: 3
The stack:
3
After reversing:
3
 
Case 3:
Please enter the elements to push: 1 2
The stack:
2
1
After reversing:
1
2
```
## 5. Python program to check whether a string is a palindrome using a stack.

Problem Description
The program prompts the user for a string and determines whether it is a palindrome with the help of a stack.

Problem Solution
1. Create a class Stack with instance variable items initialized to an empty list.
2. Define methods push, pop and is_empty inside the class Stack.
3. The method push appends data to items.
4. The method pop pops the first element in items.
5. The method is_empty returns True only if items is empty.
6. Prompt the user for a string and push all the characters to a stack.
7. Construct the reversed string by popping characters from the stack.
8. Deterime whether the string is palindromic by comparing the two strings.

Program/Source Code
Here is the source code of a Python program to check whether a string is a palindrome using a stack. The program output is shown below.
```
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
text = input('Please enter the string: ')
 
for character in text:
    s.push(character)
 
reversed_text = ''
while not s.is_empty():
    reversed_text = reversed_text + s.pop()
 
if text == reversed_text:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')
```
Program Explanation
1. An instance of Stack is created.
2. The user is prompted to enter a string.
3. The characters of the string are pushed to the stack.
4. The reversed string is constructed by popping the characters from the stack.
5. If the reversed string and the original string are the same, then the string is palindromic.
6. The result is displayed.

## Runtime Test Cases
```
Case 1:
Please enter the string: madam
The string is a palindrome.
 
Case 2:
Please enter the string: racecar
The string is a palindrome.
 
Case 3:
Please enter the string: palace
The string is not a palindrome.
```

## 6.Python program to check whether an expression is correctly parenthesized.

Problem Description
The program prompts the user for a string and determines whether it is a palindrome with the help of a stack.

Problem Solution
1. Create a class Stack with instance variable items initialized to an empty list.
2. Define methods push, pop and is_empty inside the class Stack.
3. The method push appends data to items.
4. The method pop pops the first element in items.
5. The method is_empty returns True only if items is empty.
6. Prompt the user for an expression.
7. Iterate through the characters of the expression and push to the stack if an open parenthesis is encountered and pop if a close parenthesis is encountered.
8. Determine whether the expression has balanced parentheses.

Program/Source Code
Here is the source code of a Python program to check for balanced parentheses using a stack. The program output is shown below.
```
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
exp = input('Please enter the expression: ')
 
for c in exp:
    if c == '(':
        s.push(1)
    elif c == ')':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
else:
    if s.is_empty():
        is_balanced = True
    else:
        is_balanced = False
 
if is_balanced:
    print('Expression is correctly parenthesized.')
else:
    print('Expression is not correctly parenthesized.')
```
Program Explanation
1. An instance of Stack is created.
2. The user is prompted to enter an expression.
3. Iterate through the expression and push to the stack for every open parenthesis and pop for every close parenthesis.
4. If a pop is required when the stack is empty or the stack is not empty when the expression has been iterated over, then the expression is not correctly parenthesized.
5. Display the result.

## Runtime Test Cases
```
Case 1:
Please enter the expression: (3 + 4 * (1 + (2))/(7 * (8 + 9)))
Expression is correctly parenthesized.
 
Case 2:
Please enter the expression: (a + b))(3)
Expression is not correctly parenthesized.
 
Case 3:
Please enter the expression: (4 + (3 * 2)
Expression is not correctly parenthesized.
```

