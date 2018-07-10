# coding: utf8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# coding: utf8
import random
class Solution(object):
    '''
    著名的水塘抽样，考虑n个人拿礼物，后抽的人拿到好的礼物的几率就低吗？
    '''
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n = 0
        cur = self.head
        choose = None
        while cur:
            n += 1
            p = random.randint(1, n)
            if p == 1:
                choose = cur
            cur = cur.next
        return choose.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()