class listNode:
    def __init__(self, val):
        self.data = val
        self.next = None


class singlyLinkList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = listNode(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def traverse(self):

        if not self.head:
            print("sll is empty")

        else:
            current = self.head

            while current is not None:
                print(current.data, end=" ")

                current = current.next

            print()


sll = singlyLinkList()

sll.append(10)
sll.append(20)
sll.append(30)

sll.traverse()