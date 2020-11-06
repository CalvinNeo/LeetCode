# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        D = {}

        def R(X):
            if X in D:
                return D[X]
            D[X] = Node(X.val, None, None)
            return  D[X]

        if not head:
            return head

        ori = head
        cur = R(head)
        new_head = cur
        # print "Cur {} Ori {}".format(cur.val, ori.val)
        while ori and cur:
            # print "Cur {} Ori {}".format(cur.val, ori.val)
            if ori.next:
                cur.next = R(ori.next)
            if ori.random:
                cur.random = R(ori.random)
            ori = ori.next
            cur = cur.next

        return new_head

def make_list(arr):
    head = Node(0, None, None)
    cur = head
    lst = []
    for [v, r] in arr:
        cur.next = Node(v, None, None)
        lst.append(cur.next)
        cur = cur.next

    head = head.next
    for i in xrange(len(lst)):
        [v, r] = arr[i]
        # print "i {} v {} r {} ".format(i, v, r)
        if not r is None:
            lst[i].random = lst[r]

    cur = head
    while cur:
        # print "val {} nextV {} random {}".format(cur.val, cur.next.val if cur.next else None, cur.random)
        cur = cur.next
    return head

null = None

def print_list(head):
    lst = []
    Index = {}
    cur = head
    while cur:
        # print "val {} random {}".format(cur.val, cur.random)
        lst.append(cur)
        Index[cur] = len(lst) - 1
        cur = cur.next
    ans = []
    for i in xrange(len(lst)):
        # print "val {} random {}".format(lst[i].val, lst[i].random)
        if lst[i].random:
            ans.append([lst[i].val, Index[lst[i].random]])
        else:
            ans.append([lst[i].val, None])
    return ans

sln = Solution()

L = make_list([[7,null],[13,0],[11,4],[10,2],[1,0]])
print print_list(sln.copyRandomList(L))
