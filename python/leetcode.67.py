class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = map(int, a)
        b = map(int, b)
        print a, b
        def level(x, y):
            length = max(len(x), len(y))
            if len(x) < length:
                x = [0] * (length - len(x)) + x
            elif len(y) < length:
                y = [0] * (length - len(y)) + y
            return x, y
        a, b = level(a, b)
        def allzero(lst):
            for i in lst:
                if i != 0:
                    return False
            return True
        base = a
        carry = b
        while not allzero(carry):
            combined = zip(base, carry)
            base = map(lambda p: p[0] ^ p[1], combined)
            carry = map(lambda p: p[0] & p[1], combined) + [0]
            base, carry = level(base, carry)
        print base, carry
        i = 0
        while i < len(base) and base[i] == 0:
            i += 1
        ans = ''.join(map(str, base[i:]))
        return "0" if ans == "" else  ans


sln = Solution()
print sln.addBinary("0", "0")
print sln.addBinary("11", "1")