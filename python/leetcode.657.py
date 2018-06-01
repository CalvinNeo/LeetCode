class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for c in moves:
            if c == "U":
                x += 1
            elif c == "D":
                x -= 1
            elif c == "L":
                y -= 1
            elif c == "R":
                y += 1
        return x == 0 and y == 0