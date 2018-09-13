class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        x = map(int, version1.split("."))
        y = map(int, version2.split("."))
        nx = len(x)
        ny = len(y)
        if nx > ny:
            y += [0] * (nx - ny)
        if ny > nx:
            x += [0] * (ny - nx)
            
        return cmp(x, y)