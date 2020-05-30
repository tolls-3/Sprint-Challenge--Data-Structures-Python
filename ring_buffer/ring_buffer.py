from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.data = None

    def append(self, item):
        if self.dll.length < self.capacity:
            self.dll.add_to_tail(item)
            self.data = self.dll.tail

        if self.dll.length == self.capacity:
            self.data.value = item

            if self.data is self.dll.tail:
                self.data = self.dll.head

            else:
                self.data = self.data.next

    def get(self):
        buffer_lists = []
        node = self.dll.head
        while node:
            buffer_lists.append(node.value)
            node = node.next

        return buffer_lists


print(4 % 3)
