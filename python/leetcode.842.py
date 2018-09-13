class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        if n < 3:
            return []

        def check(fst, sec, st):
            i = st
            ans = [fst, sec]
            while i < n:
                nxt = str(int(fst) + int(sec))
                ll = len(nxt)
                if S[i:i+ll] == nxt:
                    fst = sec
                    sec = nxt
                    if int(nxt) >= 2 ** 31:
                        return []
                    ans.append(nxt)
                    i += ll
                else:
                    return []
            return ans

        limit1 = n
        if S[0] == '0':
            limit1 = 2
        for sec_start in xrange(1, limit1):
            limit2 = n
            if S[sec_start] == '0':
                limit2 = sec_start + 2
            for sec_end in xrange(sec_start + 1, limit2):
                ans = check(S[0:sec_start], S[sec_start:sec_end], sec_end)
                if ans and len(ans) >= 3:    
                    return map(int, ans)
        return []

# sln = Solution()
# print sln.splitIntoFibonacci("123456579")
# print sln.splitIntoFibonacci("11235813")
# print sln.splitIntoFibonacci("112358130")
# print sln.splitIntoFibonacci("0123")
# print sln.splitIntoFibonacci("1101111")
# print sln.splitIntoFibonacci("1")
# print sln.splitIntoFibonacci("0000")
# print sln.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")
