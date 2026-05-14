class DoublyLinkedList:
    def __init__(self, key = -1, val = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} #key: node
        self.capacity = capacity

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = DoublyLinkedList(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                least_used_node = self.head.next
                self.remove(least_used_node)
                del self.cache[least_used_node.key]


        
