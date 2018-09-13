def get_bit(X, i):
    mask = 1 << i
    return X & mask

class Solution(object):
    def subarrayBitwiseORsWA(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()

        n = len(A)
        if n <= 1:
            return A

        for x in A:
            s |= set([x])

        for t in xrange(n - 1):
            lst = []
            for x in A:
                for y in s:
                    lst.append(x | y)
            print set(lst)
            s |= set(lst)
        return list(s)

    def subarrayBitwiseORsTLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()

        n = len(A)
        if n <= 1:
            return n

        for i in xrange(n):
            acc = 0
            for j in xrange(i, n):
                acc |= A[j]
                s.add(acc)
        return len(s)

    def subarrayBitwiseORsWA2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()

        n = len(A)
        if n <= 1:
            return n

        K = 32
        dp = [[-1 for j in xrange(n+1)] for i in xrange(K+1)]

        for x in A:
            s.add(x)

        for k in xrange(K):
            for i in xrange(n - 1, -1, -1):
                if get_bit(A[i], k):
                    dp[k][i] = i
                else:
                    dp[k][i] = dp[k][i+1]

        # for k in xrange(2):
        #     print k, dp[k]

        ans = 0
        for i in xrange(n):
            for k in xrange(K):
                if (not get_bit(A[i], k)) and dp[k][i] != -1 and dp[k][i] > i:
                    T = A[i] | A[dp[k][i]]
                    s.add(T)
        print s
        return len(s)


    def subarrayBitwiseORs(self, A):
        # Tabulation is a list of sets, one for each number in A. 
        # Each set, at position i, is initialised to containing the element at A[i]
        n = len(A)
        tabulation = [set([A[i]]) for i in xrange(n)]
        
        # And now we need to go through, updating the sets based on the previous set.
        for i in xrange(1, n):
            for previous_result in tabulation[i - 1]: 
                tabulation[i].add(A[i] | previous_result)  
        
        # Return the number of unique numbers in the tabulation list.
        return len(set.union(*tabulation)) if len(A) > 0 else 0



sln = Solution()
# print sln.subarrayBitwiseORs([1]) # 1
# print sln.subarrayBitwiseORs([1,1,2]) # 3
# print sln.subarrayBitwiseORs([1,2,4]) # 6
# print sln.subarrayBitwiseORs([12, 15]) # 2
print sln.subarrayBitwiseORs([1,11,6,11]) # 4