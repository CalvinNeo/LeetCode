class Solution:
    # @param {integer[]} nums
    # @return {string}

    def largestNumber(self, nums):
        strs = map(str, nums)
        def str_cmp(s1, s2):
            n = len(s1)
            m = len(s2)
            for x in xrange(0, min(n, m)):
                if ord(s1[x]) > ord(s2[x]):
                    return 1
                elif ord(s1[x]) < ord(s2[x]):
                    return -1

            if n != m:
                return cmp(int(s1 + s2), int(s2 + s1))
            else:
                return 0

        if len(nums) == 0:
            return 0
        strs.sort(cmp = str_cmp, reverse = True)
        # print strs
        ans =  "".join(strs)
        if ans.count('0') == len(ans):
            return '0'
        else:
            return ans

sln = Solution()
# 9534330 3 0 98767676 111 0
print sln.largestNumber([3, 30, 34, 5, 9])
print sln.largestNumber([3])
print sln.largestNumber([])
print sln.largestNumber([7676, 76, 98])
print sln.largestNumber([1,1,1])
print sln.largestNumber([0,0])
print sln.largestNumber([2, 213, 2281])
print sln.largestNumber([2, 213, 2218])
print sln.largestNumber([4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398])

