import Queue
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not beginWord in wordList:
            wordList.append(beginWord)

        e = 0
        if endWord in wordList:
            e = wordList.index(endWord)
        else:
            return 0
        beg = wordList.index(beginWord)
        n = len(wordList)

        mat = [[] for i in xrange(n)]

        def cmp_word(a, b):
            la = len(a)
            lb = len(b)
            if la != lb:
                return False
            hit = reduce(lambda x, y: x + y,  map(lambda (x, y): 0 if x == y else 1, zip(a, b)) )
            return hit == 1

        for i in xrange(n):
            for j in xrange(n):
                if cmp_word(wordList[i], wordList[j]):
                    mat[i].append(j)
                    mat[j].append(i)

        vis = [False] * n

        q = Queue.Queue()
        q.put((beg, 1))
        while not q.empty():
            (c, deep) = q.get()
            vis[c] = True
            if c == e:
                return deep
            for i in xrange(len(mat[c])):
                if not vis[mat[c][i]]:
                    q.put((mat[c][i], deep + 1))
        # print mat
        return 0

sln = Solution()
print sln.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print sln.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
print sln.ladderLength("a", "c", ["a", "b", "c"])

