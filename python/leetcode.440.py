class Solution(object):
    def findKthNumberTLE(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = map(int, str(n))
        m = len(arr)
        prefix = []

        class Counter(object):
            def __init__(self, X):
                self.val = X
            def dec(self):
                self.val -= 1

        def valid(x):
            return int(''.join(map(str, prefix + [x]))) <= n

        def dfs(counter, pos, leading):
            if counter.val == 0:
                return 1
            if pos >= m:
                return 0

            s = 0
            e = 10
            if leading:
                s = 1
            # print "pos {} search in [{}, {}), prefix = {}, counter = {}".format(pos, s, e, str(prefix), counter.val)
            for i in xrange(s, e):
                if valid(i):
                    prefix.append(i)
                    counter.dec()
                    if dfs(counter, pos + 1, 0):
                        return 1
                    prefix.pop()
                else:
                    break

            return 0
        dfs(Counter(k), 0, 1)
        # print prefix
        return int(''.join(map(str, prefix)))

    def findKthNumberTLE2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = map(int, str(n))
        m = len(arr)
        self.prefix = ""
        self.d = {}

        class Counter(object):
            def __init__(self, X):
                self.val = X
            def dec(self):
                self.val -= 1

        def valid(x):
            if self.prefix == "":
                return 1
            return int(self.prefix + str(x)) <= n

        def dfs(counter, pos, leading):
            if counter.val == 0:
                return 1
            if pos >= m:
                return 0

            s = 0
            e = 10
            if not leading and self.prefix in self.d:
                if self.d[prefix] < counter.val:
                    counter.val -=  self.d[prefix]
                    return 0
            prevc = counter.val
            if leading:
                s = 1
            # print "pos {} search in [{}, {}), prefix = '{}', counter = {}".format(pos, s, e, self.prefix, counter.val)
            for i in xrange(s, e):
                if valid(i):
                    self.prefix += str(i)
                    counter.dec()
                    # print "choose {}, counter = {}".format(i, counter.val)
                    if dfs(counter, pos + 1, 0):
                        return 1
                    self.prefix = self.prefix[:len(self.prefix)-1]
                else:
                    break

            if not leading:
                self.d[self.prefix] = (prevc - counter.val)
            return 0
        dfs(Counter(k), 0, 1)
        # print prefix
        if self.prefix == "":
            return 0
        return int(self.prefix)

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = map(int, str(n))
        m = len(arr)
        self.prefix = ""

        class Counter(object):
            def __init__(self, X):
                self.val = X
            def dec(self):
                self.val -= 1

        def valid(x):
            if self.prefix == "":
                return 1
            return int(self.prefix + str(x)) <= n

        def dfs(counter, pos, leading):
            if counter.val == 0:
                return 1
            if pos >= m:
                return 0

            s = 0
            e = 10
            if leading:
                s = 1
            # print "pos {} search in [{}, {}), prefix = '{}', counter = {}".format(pos, s, e, self.prefix, counter.val)
            for i in xrange(s, e):
                if valid(i):
                    self.prefix += str(i)
                    counter.dec()
                    # print "choose {}, counter = {}".format(i, counter.val)
                    if dfs(counter, pos + 1, 0):
                        return 1
                    self.prefix = self.prefix[:len(self.prefix)-1]
                else:
                    break

            return 0
        dfs(Counter(k), 0, 1)
        # print prefix
        if self.prefix == "":
            return 0
        return int(self.prefix)

sln = Solution()
print sln.findKthNumber(13, 2) # 10
print sln.findKthNumber(1, 1) # 1
print sln.findKthNumber(2, 1) # 1
print sln.findKthNumber(2, 2) # 2
print sln.findKthNumber(10, 3) # 2
print sln.findKthNumber(10, 4) # 3
print sln.findKthNumber(100, 10) # 17
print sln.findKthNumber(4289384, 1922239) # 2730010