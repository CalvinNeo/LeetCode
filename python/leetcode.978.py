class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dpD = [0 for i in xrange(n + 2)]
        dpU = [0 for i in xrange(n + 2)]

        for i in xrange(n):
            dpD[i] = 1
            dpU[i] = 1

        for i in xrange(1, n):
            if arr[i] > arr[i-1]:
                dpU[i] = dpD[i-1] + 1
            elif arr[i] < arr[i-1]:
                dpD[i] = dpU[i-1] + 1

        return max(max(dpD), max(dpU))
        
sln = Solution()
print sln.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) # 5