class Solution(object):
    def carFleetWA(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position:
            return 0

        position, speed = zip(*sorted(zip(position, speed)))
        print position, speed
        rem = 0
        n = len(position)
        for i in xrange(n - 1):
            ahead_t = (target - position[i + 1]) * 1.0 / speed[i + 1]
            new_pos = (target - position[i]) * 1.0 - speed[i] * ahead_t
            if new_pos <= 0:
                print "Hit {} {}".format(i, i + 1)
                rem += 1
        return n - rem

    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        if not position:
            return 0


        n = len(position)

        ts = [(p, (target - p) * 1.0 / s) for p, s in zip(position, speed)]
        ts.sort()

        ans = 0
        for i in xrange(n - 1, -1, -1):
            p, c = ts[i]
            if p != None:
                ans += 1
                for j in xrange(i - 1, -1, -1):
                    if ts[j][0] != None and ts[j][1] <= c:
                        ts[j] = (None, ts[j][1])
        return ans

# sln = Solution()
# print sln.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) # 3
# print sln.carFleet(10, [0,4,2], [2,1,3]) # 1