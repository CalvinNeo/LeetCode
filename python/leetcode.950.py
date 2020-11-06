class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        S = sorted(deck)

        # print "S[-2] {}".format(S[-2])

        def flipR(arr):
            # print "flipR {}".format(arr[-1])
            return [arr[-1]] + arr[:-1]

        def popR(arr):
            # print "PopR {}".format(S[1-len(arr)])
            return [S[-len(arr)-1]] + arr

        if len(S) <= 1:
            return S

        A = [S[-1]]

        for i in xrange(2 * len(S) - 3):
            if i % 2 == 0:
                A = popR(A)
            else:
                A = flipR(A)

        return A

sln = Solution()
print sln.deckRevealedIncreasing([1])
print sln.deckRevealedIncreasing([1, 2])
print sln.deckRevealedIncreasing([17,13,11,2,3,5,7])
# print sln.deckRevealedIncreasing([1,2,3,4,5,6,7])