#coding: utf8

import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.lookup = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ans = False
        if not val in self.lookup:
            self.lookup[val] = set([])
        self.lookup[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.lookup[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        # 把待删除的dst和末尾的src交换，然后pop
        last_src_v = self.lst[-1]
        last_dst_v = val
        if (not val in self.lookup) or (not self.lookup[val]):
            return False
        if last_src_v == last_dst_v:
            self.lookup[last_src_v].remove(len(self.lst) - 1)
        else:
            # DST: 在已有的dst里面找到一个位置
            last_dst_i = self.lookup[last_dst_v].pop()
            # SRC: 移掉原来指向src的lookup项
            self.lookup[last_src_v].remove(len(self.lst) - 1)
            # SRC: 重新指向原来self.lookup[val]的位置
            self.lookup[last_src_v].add(last_dst_i)
            self.lst[last_dst_i] = last_src_v
        self.lst.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = random.randint(0, len(self.lst) - 1)
        return self.lst[index]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
print obj.insert(1)
print obj.remove(1)
print obj.insert(1)