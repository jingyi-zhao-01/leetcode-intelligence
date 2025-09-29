# Problem 146. LRU Cache
# Error: remove node pointers / head-tail updates -> runtime errors

class Node:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # BUG: incorrect unlink logic can break list
        node.prev.next = node.next
        # missing: node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._add_front(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self._add_front(node)
            if len(self.map) > self.cap:
                # evict LRU
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.k]
