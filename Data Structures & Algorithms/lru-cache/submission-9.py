class DoublyLinkedList:
    def __init__(self, key = -1, val = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.tail = DoublyLinkedList()
        self.head = DoublyLinkedList()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.capacity = capacity

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_to_tail(self, node):
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_tail(node)
        else:
            node = DoublyLinkedList(key, value)
            self.cache[key] = node
            self.add_to_tail(node)
            if len(self.cache) > self.capacity: #
                lru_node = self.head.next
                self.remove(lru_node)
                del self.cache[lru_node.key]
                

        
