class Stack(object):
    # constructor
    def __init__(self):
        self.stack = []
        self.numofitems = 0
    
    # checking empty
    def isempty(self):
        return self.stack == []
    
    # pushing elements
    def push(self, data):
        self.stack.append(data)
        self.numofitems += 1  # increment index
        return '{} pushed to stack'.format(data)
    
    # deleting the element
    def pop(self):
        if not self.isempty():
            self.numofitems -= 1  # decrement index
            data = self.stack.pop()
            return '{} popped from stack'.format(data)
        else:
            return 'Stack is empty. Cannot pop.'

    # peeking the top element
    def peek(self):
        if not self.isempty():
            return 'Top element of stack: {}'.format(self.stack[-1])
        else:
            return 'Stack is empty.'

    # stack size
    def stacksize(self):
        return len(self.stack)

    # display stack
    def display(self):
        if not self.isempty():
            print('Stack elements:')
            for item in reversed(self.stack):
                print(item)
        else:
            print('Stack is empty.')

# Testing
if __name__ == '__main__':
    # object creation
    s = Stack()
    print(s.push(2))
    print(s.push(5))
    print(s.push(6))
    print(s.push(9))

    # pop
    print(s.pop())
    print(s.pop())

    # peek
    print(s.peek())

    # size
    print('Size of stack:', s.stacksize())

    # display
    s.display()
