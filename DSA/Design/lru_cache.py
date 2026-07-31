import collections

class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # key -> Node
        
        # dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # internal linked list helpers --- 
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    # public API ---
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # move to front as it's now most-recently used
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove old position, will re-add to front
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)
        
        if len(self.cache) > self.cap:
            # evict fromt the back (=least recently used)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
    