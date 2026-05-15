class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        def is_valid_peak(i):
            if i-1 >= 0 and i+1 < n:
                return arr[i] > arr[i-1] and arr[i] > arr[i+1]
            else:
                return False
        def is_peak(i):
            if i-1 >= 0:
                if arr[i] < arr[i-1]:
                    return False
            if i+1 < n:
                if arr[i] < arr[i+1]:
                    return False
            return True
        def is_eq(i):
            if i-1 >= 0:
                return arr[i] == arr[i-1]
            return False
        def is_up(i):
            if i-1 >= 0:
                return arr[i] > arr[i-1]
            else:
                return False
        def is_down(i):
            if i-1 >= 0:
                return arr[i] < arr[i-1]
            else:
                return False

        maybe_first = 0
        peak = is_peak(0)
        valid_peak = is_valid_peak(0)
        ans = 0
        for i, x in enumerate(arr):
            if i == 0:
                continue
            # print "at {}, peak {}, valid peak {}".format(i, peak, valid_peak)
            if is_up(i) and peak:
                # print "reset first to {}".format(i-1)
                maybe_first = i - 1
                valid_peak = False
                peak = False
            if is_eq(i):
                # print "reset first to {}".format(i)
                maybe_first = i
                valid_peak = False
                peak = False
                continue
            if is_peak(i):
                peak = True
            if is_valid_peak(i):
                valid_peak = True
            if is_down(i):
                if valid_peak:
                    # print "opt {} {}".format(maybe_first, i)
                    ans = max(ans, i - maybe_first + 1)
                else:
                    maybe_first = i
        return ans

sln = Solution()
print sln.longestMountain([2,1,4,7,3,2,5]) # 5
print sln.longestMountain([3,2]) # 0
print sln.longestMountain([2,2]) # 0
print sln.longestMountain([1,2,1]) # 3
print sln.longestMountain([0,2,0,2,1,2,3,4,4,1]) # 3
print sln.longestMountain([1,1,0,0,1,0]) # 3
print sln.longestMountain([3,3,1,0,1,0,1,0,2,1]) # 3