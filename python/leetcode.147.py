from utils import *

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        free_head = head.next
        sorted_head = head
        # important
        sorted_head.next = None
        while free_head:
            free_next = free_head.next
            # insert free head to sorted_head
            insert_after = sorted_head
            while insert_after.val < free_head.val:
                if insert_after.next == None or insert_after.next.val >= free_head.val:
                    break
                else:
                    insert_after = insert_after.next
            if free_head.val < insert_after.val:
                # free_head is the minimum
                # print "top {}".format(free_head.val)
                free_head.next = insert_after
                sorted_head = free_head
            else:
                # print "append {}".format(free_head.val)
                free_head.next = insert_after.next
                insert_after.next = free_head
            free_head = free_next
        return sorted_head

sln = Solution()
print_linked( sln.insertionSortList(make_linked([1])) )
print_linked( sln.insertionSortList(make_linked([1, 2])) )
print_linked( sln.insertionSortList(make_linked([2, 1])) )
print_linked( sln.insertionSortList(make_linked([3, 2, 1])) )
print_linked( sln.insertionSortList(make_linked(range(200))) )