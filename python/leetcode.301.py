import Queue
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        st = set()
        q = Queue.Queue()
        def valid(ss):
            l = 0
            for i in xrange(len(ss)):
                ch = ss[i]
                if l < 0:
                    return False
                if ch == '(':
                    l += 1
                elif ch == ')':
                    l -= 1
            return l == 0
        q.put(s)
        st.add(s)
        lev = -1
        ans = []
        while not q.empty():
            ss = q.get()
            # print "Current ss = {}".format(ss)
            m = len(ss)
            if m < lev:
                # Shorter than lev, exit loop
                break
            if valid(ss):
                # print "test {} to be Valid".format(ss)
                if lev == -1 or lev == m:
                    lev = m
                    ans.append(ss)
            else:
                # Split
                # print "test {} to be No".format(ss)
                for i in xrange(m):
                    part = ss[0: i] + ss[i + 1:]
                    # print "split", ss[0: i], ss[i + 1:]
                    if not part in st:
                        st.add(part)
                        q.put(part)
        return ans
sln = Solution()
print sln.removeInvalidParentheses("a)(")
print sln.removeInvalidParentheses(")(")
print sln.removeInvalidParentheses("()())()")
print sln.removeInvalidParentheses("(a)())()")