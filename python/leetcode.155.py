class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ori = []
        self.mi = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ori.append(x)
        newmi = x
        if self.mi:
            newmi = min(x, self.mi[-1])
        self.mi.append(newmi)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.ori:
            self.ori.pop()
            self.mi.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.ori:
            return self.ori[-1]
        return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.mi:
            return self.mi[-1]
        return 0
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()