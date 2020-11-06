import random
from math import sin, cos, asin, acos, pi

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint1(self):
        """
        :rtype: List[float]
        """
        theta = random.uniform(0, 2 * pi)
        r = self.r * (random.uniform(0,1) ** 0.5)
        y = sin(theta) * r
        x = cos(theta) * r
        return [x + self.x, y + self.y]

    def randPoint(self):
        """
        :rtype: List[float]
        """
        def in_circle(x, y):
            return x ** 2 + y ** 2 <= self.r ** 2

        while 1:
            x = random.uniform(-self.r, self.r)
            y = random.uniform(-self.r, self.r)
            if in_circle(x, y):
                return [x + self.x, y + self.y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()