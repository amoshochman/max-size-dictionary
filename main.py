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

    def put(self, key, value):
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

    def get(self, key):
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


if __name__ == '__main__':
    size = 3
    my_dict = MyDict(size)
    my_dict.put(1, "one")
    my_dict.put(2, "two")
    my_dict.put(3, "three")
    my_dict.get(1)
    my_dict.get(2)
    my_dict.put(4, "four")
    assert all(elem in my_dict.data for elem in {1, 2, 4}) and 3 not in my_dict.data
