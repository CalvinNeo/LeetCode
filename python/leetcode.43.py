class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        a1 = map(int, list(num1))
        a2 = map(int, list(num2))

        self.ans = [0] * (n1 + n2)
        self.temp = []

        def simple_mul(x, offset):
            self.temp = [0] * (n1 + n2)
            carry = 0
            bit = n2 + n1 - 1
            for i in xrange(n2 - 1, -1, -1):
                res = a2[i] * x + carry
                base = res % 10
                carry = res / 10
                self.temp[bit - offset] = base
                bit -= 1
            if carry > 0:
                self.temp[bit - offset] = carry

        def simple_add():
            carry = 0
            bit = n2 + n1 - 1
            newans = [0] * (n1 + n2)
            for i in xrange(n1 + n2 - 1, -1, -1):
                # print "self.ans", self.ans
                # print "self.temp", self.temp
                res = self.ans[i] + self.temp[i] + carry
                base = res % 10
                carry = res / 10
                newans[bit] = base
                bit -= 1
            self.ans = newans

        for i in xrange(n1 - 1, -1, -1):
            # print "self.ans", self.ans
            simple_mul(a1[i], n1 - 1 - i)
            # print "self.temp", self.temp
            simple_add()

        raws = ''.join(map(str, self.ans))
        s1 = raws.lstrip('0')
        if s1 == '':
            return '0'
        else:
            return s1