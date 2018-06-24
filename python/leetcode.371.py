class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while True:
            base = (a ^ b) & 0xffffffff
            carry = (((a & b) & 0xffffffff) << 1) & 0xffffffff
            if carry == 0:
                break
            a = carry
            b = base
        if base & 0x80000000:
            return -(((~base) + 1) & 0x7fffffff)
            return -(0xffffffff - base + 1)
        return base