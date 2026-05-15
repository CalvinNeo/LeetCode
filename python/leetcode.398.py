import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.m = {}
        for i, x in enumerate(nums):
            if x in self.m:
                self.m[x].append(i)
            else:
                self.m[x] = [i]
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = random.randint(0, len(self.m[target]) - 1)
        return self.m[target][index]