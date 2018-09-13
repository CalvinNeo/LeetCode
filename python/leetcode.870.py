import bisect
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        ans = []
        A.sort()
        for x in B:
            i = bisect.bisect_left(A, x + 1)
            if i >= len(A):
                ans.append(A[0])
                del A[0]
            else:
                ans.append(A[i])
                del A[i]
        return ans 

sln = Solution()
'''
[2, 11, 7, 15]
[24, 32, 8, 12]
[2,0,2,1,4]
'''
print sln.advantageCount([2,7,11,15], [1,10,4,11])
print sln.advantageCount([12,24,8,32], [13,25,32,11])
print sln.advantageCount([2,0,4,1,2], [1,3,0,0,2])