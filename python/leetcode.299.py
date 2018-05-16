class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnta = sum(map(lambda (x, y): 1 if x == y else 0, zip(secret, guess)))
        cntb = 0
        dguess = {i: guess.count(i) for i in guess}
        dsecret = {i: secret.count(i) for i in secret}

        for k, v in dsecret.iteritems():
            if k in dguess:
                cntb += min(v, dguess[k])

        return "{}A{}B".format(cnta, cntb - cnta)

sln = Solution()
print sln.getHint("0123", "0123")
print sln.getHint("0123", "9999")
print sln.getHint("1807", "7810")
print sln.getHint("1123", "0111")
print sln.getHint("11", "10")