class DLink(object):
    def __init__(self, key, val, p, n):
        self.prev = p
        self.next = n
        self.val = val
        self.key = key

    def __str__(self):
        return "({}:{})".format(self.key, self.val)

class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.head = None
        self.tail = None
        self.zero = None
        # Always add zero to self.zero.next

    def add_node(self, key):
        if not self.head:
            # No node in linked list
            nd = DLink(key, 0, None, None)
            self.head = nd
            self.tail = nd
            self.zero = nd
            return nd
        else:
            if self.zero == None:
                # All > 0
                nd = DLink(key, 0, None, self.head)
                self.head.prev = nd
                self.head = nd
            else:
                nd = DLink(key, 0, self.zero, self.zero.next)
                if self.zero:
                    self.zero.next = nd
                if self.zero.next:
                    self.zero.next.prev = nd

            if not nd.next:
                self.tail = nd

            # self.zero will be updated later
            return nd

    def del_node(self, nd):
        if self.zero == nd:
            self.zero = nd.prev
        if self.head == nd:
            self.head = nd.next
        if self.tail == nd:
            self.tail = nd.prev

        if nd.prev:
            nd.prev.next = nd.next
        if nd.next:
            nd.next.prev = nd.prev

    def swap_node(self, cur, nxt):
        pp = cur.prev
        nn = nxt.next

        if pp:
            pp.next = nxt
        else:
            self.head = nxt

        nxt.prev = pp
        nxt.next = cur

        cur.prev = nxt
        cur.next = nn

        if nn:
            nn.prev = cur
        else:
            self.tail = cur

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if not key in self.keys:
            self.keys[key] = self.add_node(key)
        nd = self.keys[key]
        nd.val += 1

        if self.zero == nd:
            cur = nd
            # cur <= 0 or cur = None
            while cur and cur.val > 0:
                cur = cur.prev
            if not cur:
                self.zero = None
            else:
                self.zero = cur

        elif self.zero and nd.val <= 0 and self.zero.val < nd.val:
            self.zero = nd

        elif not self.zero and nd.val <= 0:
            self.zero = nd

        # print "nd1", nd, nd.prev, nd.next
        while nd.next and nd.next.val < nd.val:
            self.swap_node(nd, nd.next)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if not key in self.keys:
            self.keys[key] = self.add_node(key)
        nd = self.keys[key]
        nd.val -= 1
        if nd.val <= 0:
            self.del_node(nd)
            return

        if self.zero == nd:
            cur = nd
            while cur.next and cur.next.val <= 0:
                cur = cur.next
            self.zero = cur

        elif self.zero and nd.val <= 0 and self.zero.val < nd.val:
            self.zero = nd

        elif not self.zero and nd.val <= 0:
            self.zero = nd

        # print "nd2", nd, nd.prev, nd.next
        while nd.prev and nd.prev.val > nd.val:
            self.swap_node(nd.prev, nd)


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail:
            return self.tail.key
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head:
            return self.head.key
        else:
            return ""
        
def print_linked(head):
    while head != None:
        print "({}:{} [{},{}])".format(head.key, head.val, head.prev, head.next), " ",
        head = head.next
    print ""

# # Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc('a')
# # print_linked(obj.head); print "Zero", obj.zero
# obj.dec('b')
# # print_linked(obj.head); print "Zero", obj.zero
# print obj.getMaxKey()
# print obj.getMinKey()
# obj.dec('a')
# # print_linked(obj.head); print "Zero", obj.zero
# obj.dec('a')
# # print_linked(obj.head); print "Zero", obj.zero
# obj.dec('a')
# # print_linked(obj.head); print "Zero", obj.zero
# print obj.getMinKey()

# obj.inc('a')
# # print obj.head, obj.head.prev, obj.head.next
# # print obj.tail, obj.tail.prev, obj.tail.next
# # print "========="
# print_linked(obj.head); print "Zero", obj.zero; print "========="
# obj.inc('b')
# # print obj.head, obj.head.prev, obj.head.next
# # print obj.tail, obj.tail.prev, obj.tail.next
# # print "========="
# print_linked(obj.head); print "Zero", obj.zero; print "========="
# obj.dec('a')
# # print obj.head, obj.head.prev, obj.head.next
# # print obj.tail, obj.tail.prev, obj.tail.next
# # print "========="
# print_linked(obj.head); print "Zero", obj.zero; print "========="

# print obj.getMinKey()

# obj = AllOne()
# obj.dec("hello")
# print obj.getMaxKey()