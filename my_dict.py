import typing

class Node:
    def __init__(self):
        self.next = None
        self.previous = None
        self.value = None


class MyDict:
    def __init__(self, size):
        self.size = size
        self.data = {}
        self.head = None
        self.tail = None

    def put(self, key: typing.Hashable, value):
        if key in self.data:
            self.move_node_to_tail(self, self.data[key])
        else:
            node = Node()
            self.insert_at_tail(node)
            self.data[key] = node
            if self.size < len(self.data):
                self.remove_head()
        self.data[key].key = key
        self.data[key].value = value

    def get(self, key: typing.Hashable):
        if key not in self.data:
            raise ValueError("key " + str(key) + " was not found in My Dict")
        node = self.data[key]
        self.move_node_to_tail(node)
        return node.value

    def insert_at_tail(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

    def move_node_to_tail(self, node):
        if node == self.tail:
            return
        if node == self.head:
            self.head = node.next
        else:
            node.previous.next = node.next
        node.previous = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    def remove_head(self):
        previously_head = self.head
        self.head = self.head.next
        self.head.previous = None
        del self.data[previously_head.key]