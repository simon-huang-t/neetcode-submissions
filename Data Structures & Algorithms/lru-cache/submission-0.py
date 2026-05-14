class DoublyLinkedList:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoublyLinkedList(-1, -1)
        self.tail = DoublyLinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
        else:
            node = DoublyLinkedList(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                first_node = self.head.next
                self.remove(first_node)
                del self.cache[first_node.key]



    def insert(self, node):
        prev = self.tail.prev
        node.next = self.tail
        prev.next = node
        node.prev = prev
        self.tail.prev = node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        












