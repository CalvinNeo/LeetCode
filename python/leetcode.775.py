class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        '''
        A[i] < A[j] for all j > i + 1
        '''
        mmx = 0
        for j in xrange(2, n):
            mmx = max(A[j - 2], mmx)
            if not mmx < A[j]:
                return False
        return True