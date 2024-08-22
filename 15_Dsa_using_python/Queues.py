class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def display(self):
        print("Queue:", self.queue)


# Testing the Queue class
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.display()  # Output: Queue: [1, 2, 3, 4]
    print("Size of queue:", q.size())  # Output: Size of queue: 4
    print("Dequeued item:", q.dequeue())  # Output: Dequeued item: 1
    q.display()  # Output: Queue: [2, 3, 4]
    print("Peeked item:", q.peek())  # Output: Peeked item: 2
