class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.n = k + 1
        self.buf = [None for i in xrange(self.n + 1)]
        self.head = 0
        self.tail = 0
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.head -= 1
        self.buf[self.h()] = value
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.buf[self.t()] = value
        self.tail += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head += 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.tail -= 1
        return True
        
    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.buf[self.h()]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.buf[self.r()]

    def h(self):
        return (self.head + self.n) % self.n

    def t(self):
        return (self.tail + self.n) % self.n

    def r(self):
        return (self.tail + self.n - 1) % self.n

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.h() == self.t()

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.tail + 1) % self.n == self.head % self.n

# Your MyCircularDeque object will be instantiated and called as such:
myCircularDeque = MyCircularDeque(3);
print myCircularDeque.insertLast(1);  #// return True
print myCircularDeque.insertLast(2);  #// return True
print myCircularDeque.insertFront(3); #// return True
print myCircularDeque.insertFront(4); #// return False, the queue is full.
print myCircularDeque.getRear();      #// return 2
print myCircularDeque.isFull();       #// return True
print myCircularDeque.deleteLast();   #// return True
print myCircularDeque.insertFront(4); #// return True
print myCircularDeque.getFront();     #// return 4

obj = MyCircularDeque(4)
print obj.insertFront(9)
print obj.deleteLast()
print obj.getRear()
print obj.getFront()
print obj.getFront()
print obj.deleteFront()
print obj.insertFront(6)
print obj.insertLast(5)
print obj.insertFront(9)
print obj.getFront()
print obj.insertFront(6)

obj = MyCircularDeque(3)
print obj.insertFront(9)
print obj.getRear()
print obj.insertFront(9)
print obj.getRear()
print obj.insertLast(5)
print obj.getFront()
print obj.getRear()
print obj.getFront()
print obj.insertLast(8)
print obj.deleteLast()
print obj.getFront()