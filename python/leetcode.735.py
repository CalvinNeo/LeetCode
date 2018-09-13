class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        for i in xrange(n):
            if asteroids[i] < 0:
                for j in xrange(i - 1, -1, -1):
                    if asteroids[j] > 0:
                        if abs(asteroids[j]) < abs(asteroids[i]):
                            asteroids[j] = 0
                        elif abs(asteroids[j]) > abs(asteroids[i]):
                            asteroids[i] = 0
                            break
                        else:
                            asteroids[i] = 0
                            asteroids[j] = 0
        return filter(lambda x: x != 0, asteroids)

# sln = Solution()
# print sln.asteroidCollision([5, 10, -5])
# print sln.asteroidCollision([8, -8])
# print sln.asteroidCollision([10, 2, -5])
# print sln.asteroidCollision([-2, -1, 1, 2])