class BiNode(object):
    def __init__(self, k, x):
        self.prev = None
        self.next = None
        self.key = k
        self.val = x

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = dict()
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def enqueue(self, node):
        self.data[node.key] = node
        if self.head == None:
            assert self.tail == None
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def remove(self, node):
        self.data.pop(node.key)
        if node.next:
            node.next.prev = node.prev
        else:
            # node is tail
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            # node is head
            self.head = node.next

        self.size -= 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
            # find old_node and remove it
            value = self.data[key].val
            self.remove(self.data[key])
            self.enqueue( BiNode(key, value) )

            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data:
            # find old_node and remove it
            self.remove(self.data[key])
            self.enqueue( BiNode(key, value) )

        else:
            self.enqueue( BiNode(key, value) )

        if self.size > self.capacity:
            self.remove(self.head)

if __name__ == '__main__':
    # cache = LRUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print cache.get(1)
    # cache.put(3, 3)
    # print cache.get(2)
    # cache.put(4, 4)
    # print cache.get(1)
    # print cache.get(3)
    # print cache.get(4)

    # print "==========="

    # cache = LRUCache(2)
    # cache.put(2, 1)
    # cache.put(1, 1)
    # cache.put(2, 3)
    # cache.put(4, 1)
    # print cache.get(1)
    # print cache.get(2)

    # print "==========="

    # cache = LRUCache(2)
    # print cache.get(2)
    # print cache.get(2)
    # cache.put(2, 6)
    # print cache.get(1)
    # cache.put(1, 5)
    # print "size", cache.size
    # cache.put(1, 2)
    # print cache.get(1)
    # print cache.get(2)

    print "==========="

    # cache = LRUCache(2)
    # print cache.get(1)
    # cache.put(1, 1)
    # print cache.get(1)
    # cache.put(1, 2)
    # print cache.get(1)
    # cache.put(2, 3)
    # print cache.get(2)
    # cache.put(3, 5)
    # cache.put(1, 4)
    # print cache.get(2)

    print "==========="
    cache = LRUCache(1)
    cache.put(2, 1)
    cache.put(3, 2)
    print cache.get(3)
    print cache.get(2)
