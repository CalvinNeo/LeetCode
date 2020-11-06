import threading


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.num = 0
        self.fooi = 0
        self.bari = 0

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        while self.fooi < self.n:
            self.lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            if self.num == 0:
                printFoo()
                self.num = 1
                self.fooi += 1
            self.lock.release()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        while self.bari < self.n:
            self.lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            if self.num == 1:
                printBar()
                self.num = 0
                self.bari += 1
            self.lock.release()

def printFoo():
    print "foo",
def printBar():
    print "bar",

foobar = FooBar(6)
t1 = threading.Thread(target=foobar.foo, args=(printFoo,))
t1.start()
t2 = threading.Thread(target=foobar.bar, args=(printBar,))
t2.start()