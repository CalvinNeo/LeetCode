class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        length = len(digits)
        digits[-1] += 1
        for i in xrange(length-1, -1, -1):
            digits[i] += carry
            carry = digits[i] / 10
            digits[i] = digits[i] % 10
        if carry != 0:
            return [1] + digits
        else:
            return digits