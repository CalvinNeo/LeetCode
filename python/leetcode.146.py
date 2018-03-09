class LRUCache(object):
    import Queue
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = dict()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.data:
            return -1
        else:
            self.size -= 1
            ans = self.data[key]
            self.data[key] = -1
            return ans

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.size > self.capacity:
            pass
        else:
            self.size += 1
        self.data[key] = value
