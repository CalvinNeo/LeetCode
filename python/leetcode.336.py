class Node(object):
    def __init__(self, x, ending):
        self.x = x
        self.ending = ending
        self.next = {}

def is_parli(x):
    ll = len(x)
    if ll == 0:
        return 1
    for i in xrange((ll - 1) / 2 + 1):
        if x[i] != x[ll - i - 1]:
            return 0
    return 1


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        root = Node(None, -1)

        for j, w in enumerate(words):
            ll = len(w)
            cur = root
            for i in xrange(ll - 1, -1, -1):
                if not w[i] in cur.next:
                    cur.next[w[i]] = Node(w[i], -1)
                cur = cur.next[w[i]]
            cur.ending = j

        stk = []
        def dfs(cur, res):
            # print "stk", stk
            if cur.ending != -1:
                if is_parli(stk):
                    res.append(cur.ending)
            for k, v in cur.next.iteritems():
                stk.append(k)
                dfs(v, res)
                stk.pop()

        def find_p(cur):
            res = []
            dfs(cur, res)
            return res

        ans = set()
        for j, w in enumerate(words):
            ll = len(w)
            cur = root
            # print "======== j = {}".format(j)
            flag = 1
            for i in xrange(ll):
                if cur.ending != -1 and cur.ending != j and is_parli(w[i:ll]):
                    # Pattern end
                    # print "j {} cur.ending {}".format(j, cur.ending)
                    ans.add((j, cur.ending))
                if w[i] in cur.next:
                    # print "jump to {} i = {}/{}".format(w[i], i, ll)
                    cur = cur.next[w[i]]
                else:
                    flag = 0
                    break
            # If there leaving some pattern
            # print cur.x, cur.ending
            if flag:
                if cur.ending != -1 and cur.ending != j:
                    ans.add((j, cur.ending))
                for inner in find_p(cur):
                    # print "j {} inner {}".format(j, inner)
                    if inner != j:
                        ans.add((j, inner))

        return map(list, ans)

# sln = Solution()
# print sln.palindromePairs(["abcd","dcba","lls","s","sssll"])
# print sln.palindromePairs(["bat","tab","cat"])
# print sln.palindromePairs(["a",""])
# print sln.palindromePairs(["a","abc","aba",""])
# print sln.palindromePairs(["aba",""])