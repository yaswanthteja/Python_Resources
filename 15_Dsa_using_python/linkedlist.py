class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("Linked list is empty. Cannot delete.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty. Cannot delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Testing the LinkedList class
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.display()  # Output: 2 -> 3 -> 4 -> 5 -> None
    ll.delete_at_beginning()
    ll.display()  # Output: 3 -> 4 -> 5 -> None
    ll.delete_at_end()
    ll.display()  # Output: 3 -> 4 -> None
