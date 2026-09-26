class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.root = ListNode(-1, -1)
        self.end = ListNode(-1, -1)
        self.root.next = self.end
        self.end.prev = self.root
        self.max = capacity
        self.cap = 0
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.moveToEnd(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.moveToEnd(node)
        else:
            node = ListNode(key, value)
            self.insertNode(node)
            if self.cap == self.max:
                lru = self.root.next
                self.removeNode(self.root.next)
                del self.map[lru.key]
            else:
                self.cap += 1
        self.map[key] = node

    def moveToEnd(self, node):
        self.removeNode(node)
        self.insertNode(node)

    def insertNode(self, node):
        prev, next = self.end.prev, self.end
        prev.next = node
        node.prev = prev
        next.prev = node
        node.next = next

    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
