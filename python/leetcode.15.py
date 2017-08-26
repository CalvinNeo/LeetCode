class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        uni = []
        for x in nums:
            if d.has_key(x):
                d[x] += 1
            else:
                uni.append(x)
                d[x] = 1
        ans = []
        for i in xrange(len(uni)):
            d[uni[i]] -= 1
            for j in xrange(len(uni)):
                if d.has_key(uni[j]) and d[uni[j]] > 0:
                    d[uni[j]] -= 1
                    k = 0 - uni[i] - uni[j]
                    if uni[i] >= uni[j] >= k:
                        if d.has_key(k) and d[k] > 0:
                            ans.append([uni[i], uni[j], k])
                    d[uni[j]] += 1
            d[uni[i]] += 1
        return ans
    
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        uni = []
        for x in nums:
            if d.has_key(x):
                d[x] += 1
            else:
                uni.append(x)
                d[x] = 1
        uni.sort()
        ans = []
        for i in xrange(len(uni)):
            d[uni[i]] -= 1
            l = i
            r = len(uni) - 1
            while l <= r:
                d[uni[l]] -= 1
                d[uni[r]] -= 1
                s = uni[i] + uni[l] + uni[r]
                if s == 0:
                    if d[uni[l]] >= 0 and d[uni[r]] >= 0:
                        ans.append([uni[i], uni[l], uni[r]])
                    d[uni[l]] += 1
                    d[uni[r]] += 1 
                    l += 1; r -= 1
                elif s > 0:
                    d[uni[l]] += 1
                    d[uni[r]] += 1 
                    r -= 1
                elif s < 0:
                    d[uni[l]] += 1
                    d[uni[r]] += 1 
                    l += 1
            d[uni[i]] += 1
        return ans


class Solution3(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        uni = []
        for x in nums:
            if d.has_key(x):
                d[x] += 1
            else:
                uni.append(x)
                d[x] = 1
        uni.sort()
        ans = []
        for i in xrange(len(uni)):
            d[uni[i]] -= 1
            for j in xrange(i, len(uni)):
                if d.has_key(uni[j]) and d[uni[j]] > 0:
                    d[uni[j]] -= 1
                    k = 0 - uni[i] - uni[j]
                    if k < uni[0]:
                        d[uni[j]] += 1
                        break
                    if uni[i] <= uni[j] <= k:
                        if d.has_key(k) and d[k] > 0:
                            ans.append([uni[i], uni[j], k])
                    d[uni[j]] += 1
            d[uni[i]] += 1
        return ans

sln = Solution3()
print sln.threeSum([0, 0, 0])
print sln.threeSum([0, 1, -1])
print sln.threeSum([0, 0, 0, 1, 1, -2])
print sln.threeSum([-1, 0, 1, 2, -1, -4])
print sln.threeSum([1,1,-2])

print "aaaa"

sln = Solution2()
print sln.threeSum([0, 0, 0])
print sln.threeSum([0, 1, -1])
print sln.threeSum([0, 0, 0, 1, 1, -2])
print sln.threeSum([-1, 0, 1, 2, -1, -4])
print sln.threeSum([1,1,-2])
