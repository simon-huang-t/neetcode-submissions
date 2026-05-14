class DoublyLinkedList:
    def __init__(self, key = -1 , val = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # (key: node)
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.insert_node(node)
        else:
            node = DoublyLinkedList(key, value)
            self.insert_node(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                oldest_node = self.head.next
                self.remove_node(oldest_node)
                del self.cache[oldest_node.key]


    def remove_node(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert_node(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev
        
        self.tail.prev = node
        node.next = self.tail

        
