class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    # Delete by value
    def delete_by_value(self, value):

        # If linked list is empty
        if self.head is None:
            print("Linked List is empty")

        # If head node contains value
        elif self.head.data == value:
            self.head = self.head.next

        else:
            current = self.head

            while current.next is not None and current.next.data != value:
                current = current.next

            # If value found
            if current.next is not None:
                current.next = current.next.next

            else:
                print("Value not found")

    # Traverse 
    # linked list
    def traverse(self):

        if self.head is None:
            print("Linked List is empty")

        else:
            current = self.head

            while current is not None:
                print(current.data, end=" -> ")
                current = current.next

            print("None")


# Driver code
ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print("Before deletion:")
ll.traverse()

ll.delete_by_value(20)

print("After deletion:")
ll.traverse()