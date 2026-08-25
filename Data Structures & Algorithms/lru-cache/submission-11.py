class DoublyLinkedList:

    def __init__(self, key = - 1, val = - 1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_to_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_to_tail(node)
        else:
            node = DoublyLinkedList(key, value)
            self.cache[key] = node
            self.add_to_tail(node)
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self.remove_node(lru_node)
                del self.cache[lru_node.key]

        
