# coding: utf8
# http://wowaccepted.com/2018/03/04/leetcod-753-cracking-the-safe%E9%A2%98%E7%9B%AE%E8%A7%A3%E6%9E%90/
class Solution(object):
    def crackSafe1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        '''
        00 -> 01 -> 11 -> 10 -> 00
               |    |
               ------
        '''
        vis = set()
        ans = '0' * (n - 1)
        cur = n - 1
        tot = k ** n
        while tot:
            for j in xrange(k - 1, -1, -1):
                passwd = ans[cur-(n-1):cur] + str(j)
                if not passwd in vis:
                    vis |= set([passwd])
                    tot -= 1
                    cur += 1
                    ans += str(j)
                    # print "new pass", passwd, "new ans", ans
                    break
        return ans

    def crackSafeWA(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        st = '0' * n
        self.vis = set()
        self.path = st
        tot = k ** n

        def dfs(u):
            l = len(self.path)
            prev_state = self.path[l-n:l]
            prefix = self.path[l-(n-1):l]
            print "begin state {}, current set {}, prefix {}, path {}".format(u, str(self.vis), prefix, self.path)
            for j in xrange(k - 1, -1, -1):
                next_state = prefix + str(j)
                edge_name = prev_state + "," + next_state
                if not (edge_name in self.vis) and not next_state == prev_state:
                    self.vis |= set([edge_name])
                    if len(self.vis) >= tot:
                        return
                    self.path += next_state[-1]
                    # print 'next_state', next_state
                    dfs(next_state)
                    if len(self.vis) >= tot:
                        return

        ans = dfs(st)
        # print self.vis
        return self.path


    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        st = '0' * n
        # self.vis = set()
        self.visp = set()
        self.path = st
        tot = k ** n

        def dfs(prev_state):
            l = len(self.path)
            prev_state = self.path[l-n:l]
            prefix = self.path[l-(n-1):l]
            # print "begin state {}, current set {}, prefix {}, path {}".format(prev_state, str(self.vis), prefix, self.path)
            for j in xrange(k - 1, -1, -1):
                next_state = prefix + str(j)
                edge_name = prev_state + "," + next_state
                if not (next_state in self.visp) and not next_state == prev_state:
                    # self.vis |= set([edge_name])
                    self.visp |= set([next_state])
                    # if len(self.vis) >= tot:
                        # return
                    if len(self.visp) > tot:
                        return
                    self.path += next_state[-1]
                    # print 'next_state', next_state
                    dfs(next_state)
                    # if len(self.vis) >= tot:
                        # return
                    if len(self.visp) > tot:
                        return

        self.visp = set([st])
        ans = dfs(st)
        # print self.vis
        return self.path

sln = Solution()
print sln.crackSafe(1, 2) # 01
print sln.crackSafe(2, 2) # 00110
print sln.crackSafe(1, 4) # 0321