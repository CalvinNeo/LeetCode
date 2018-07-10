class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        S = list(senate)
        cnt = 0
        n = len(senate)
        r_left = 0
        d_left = 0
        for i in S:
            if i == 'R':
                r_left += 1
            else:
                d_left += 1
        i = 0
        while r_left and d_left:
            j = i % n
            if S[j] == 'R':
                if cnt < 0:
                    S[j] = ''
                    r_left -= 1
                cnt += 1
            elif S[j] == 'D':
                if cnt > 0:
                    S[j] = ''
                    d_left -= 1
                cnt -= 1
            i += 1
        if r_left:
            return "Radiant"
        else:
            return "Dire"