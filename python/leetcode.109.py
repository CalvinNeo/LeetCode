# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_list(A):
    root = ListNode(0)
    cur = root
    for x in A:
        cur.next = ListNode(x)
        cur = cur.next
    return root.next

def print_list(N):
    root = N
    while root != None:
        print root.val,
        root = root.next

def print_tree(T, deep = 0):
    if T:
        print "  " * deep, T.val
    if T.left:
        print_tree(T.left, deep + 1)
    if T.right:
        print_tree(T.right, deep + 1)

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast = head
        slow = head
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        # print "slow.val", slow.val, head.val, slow.next, pre.val
        pre.next = None
        if head:
            root.left = self.sortedListToBST(head)
        if slow.next:
            root.right = self.sortedListToBST(slow.next)
        return root

sln = Solution() 
print_tree( sln.sortedListToBST(make_list([-3, 10])) )
print_tree( sln.sortedListToBST(make_list([-10,-3,0,5,9])))
