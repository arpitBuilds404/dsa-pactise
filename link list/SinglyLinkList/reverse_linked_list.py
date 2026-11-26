# Problem: Reverse a Linked List
# Given the head of a singly linked list, reverse the list and return its new head.
#
# Example:
# Input:  1 -> 2 -> 3 -> 4 -> None
# Output: 4 -> 3 -> 2 -> 1 -> None
#
# Approach: Iteratively reverse each node's next pointer.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next  # Save the next node
            current.next = previous   # Reverse the current link
            previous = current        # Move previous forward
            current = next_node       # Move current forward

        self.head = previous

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Driver code
ll = LinkedList()

for value in [1, 2, 3, 4]:
    ll.insert_at_end(value)

print("Original linked list:")
ll.traverse()

ll.reverse()

print("Reversed linked list:")
ll.traverse()
