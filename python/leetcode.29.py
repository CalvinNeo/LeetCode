
class Solution(object):
    def add(self, a, b):
        while True:
            s = a ^ b
            carry = (a & b) << 1
            if s == 0:
                return carry
            elif carry == 0:
                return s
            else:
                a = s
                b = carry

    def sub(self, a, b):
        t = self.add((~b), 1)
        print a, t
        return self.add(a, t)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 9223372036854775807
        elif dividend == 0:
            return 0
        n = 0
        a = abs(dividend)
        b = abs(divisor)
        sgn1 = dividend / a
        sgn2 = divisor / b

        while a >= b:
            t = b
            l = 1
            while a > t + t:
                t = t + t
                l = l + l
            a -= t
            n += l

        res = sgn1 * sgn2 * n
        # Add this code to pass the test
        # PYTHON'S INT WILL NEVER OVERFLOW
        return min(max(-2147483648, res), 2147483647)

sln = Solution()
print sln.divide(-100, -1)


        # while a >= b:
        #     t = b
        #     l = 1
        #     while a >= t:
        #         a -= t
        #         n += l
        #         t = t + t
        #         l = l + l
