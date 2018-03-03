def se(arr, fr, to):
    if to == fr:
        return arr[fr]
    elif to - fr == 1:
        return min(arr[to], arr[fr])
    mid = (fr + to) / 2
    if arr[fr] > arr[mid]:
        return se(arr, fr, mid)
    elif arr[mid + 1] > arr[to]:
        return se(arr, mid + 1, to)
    else:
        return arr[mid + 1]

class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = True
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = False
                break
        if not flag:
            return se(nums, 0, len(nums) - 1)
        else:
            return nums[0]

sln = Solution()
print sln.findMin([1,2,3,4,5,6])
print sln.findMin([4,5,6,1,2,3])
print sln.findMin([2,3,1])
print sln.findMin([3,1,2])
print sln.findMin([2,1])
print sln.findMin([3,4,1,2])
print sln.findMin([2,3,4,1])