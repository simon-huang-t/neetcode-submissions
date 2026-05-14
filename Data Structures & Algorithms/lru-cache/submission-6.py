#1 error
# 2 errors
class DoublyLinkedList:
    def __init__(self, key = -1, val = -1, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key: node
        self.head = DoublyLinkedList() 
        self.tail = DoublyLinkedList() 
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)
        return node.val #here forgot .val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.insert_node(node)
        else:
            node = DoublyLinkedList(key, value)
            self.cache[key] = node
            self.insert_node(node)
            if len(self.cache) > self.capacity:
                oldest_node = self.head.next
                self.remove_node(oldest_node)
                del self.cache[oldest_node.key]









        
