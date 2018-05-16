import Queue
class Solution(object):
    def ladderLength1(self, beginWord, endWord, wordList):
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

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        delta = 0
        if not beginWord in wordList:
            delta = 1
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

        vis = [0] * n

        # Search from beg to e

        q1 = Queue.Queue()
        q2 = Queue.Queue()
        q1.put((beg, 1))
        q2.put((e, -1))
        vis[beg] = 1
        vis[e] = -1

        def sgn(x):
            if x == 0: return x
            return x / abs(x)

        def bfs(q, flag):
            c, d = q.get()
            for i in xrange(len(mat[c])):
                if sgn(vis[mat[c][i]]) != flag:
                    print "{} {}: {} -> {}".format("q1" if flag > 0 else "q2", d, wordList[c], wordList[mat[c][i]])
                    if sgn(vis[mat[c][i]]) == -flag:
                        return True, abs(d - vis[mat[c][i]])
                    else:
                        vis[mat[c][i]] = d + flag
                        q.put((mat[c][i], d + flag))
            return False, 0

        while (not q1.empty()) or (not q2.empty()):
            flag = 0
            if not q1.empty():
                ans, d = bfs(q1, 1)
                if ans:
                    return d
            if not q2.empty():
                ans, d = bfs(q2, -1)
                if ans:
                    return d

        # print mat
        return 0


sln = Solution()
# 0 5 5 0 2 5 4 4
# print sln.ladderLength("hot", "dog", ["hot", "dog"]) # 0
print sln.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5
# print sln.ladderLength("hit", "cog", ["hot","dot","dog","cog"]) # 5
# print sln.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) # 0
# print sln.ladderLength("a", "c", ["a", "b", "c"]) # 2
# print sln.ladderLength("kiss", "tusk", ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]) # 5
# print sln.ladderLength("cat", "fin", ["cat", "fat", "fin", "fit"]) # 4
# print sln.ladderLength("cat", "fin", ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]) # 4
