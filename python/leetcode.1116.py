import threading

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.cond = threading.Condition()
        self.index = 0

        
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while 1:
            if self.cond.acquire():
                if self.index >= self.n * 2:
                    self.cond.notify()
                    self.cond.release()
                    break
                elif self.index % 2 == 0:
                    printNumber(0)
                    self.index += 1
                    self.cond.notify()
                else:
                    self.cond.wait()
                self.cond.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while 1:
            if self.cond.acquire():
                if self.index >= self.n * 2:
                    self.cond.notify()
                    self.cond.release()
                    break
                elif self.index % 4 == 3:
                    printNumber((self.index + 1) / 2)
                    self.index += 1
                    self.cond.notify()
                else:
                    self.cond.wait()
                self.cond.release()
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while 1:
            if self.cond.acquire():
                if self.index >= self.n * 2:
                    self.cond.notify()
                    self.cond.release()
                    break
                elif self.index % 4 == 1:
                    printNumber((self.index + 1) / 2)
                    self.index += 1
                    self.cond.notify()
                else:
                    self.cond.wait()
                self.cond.release()