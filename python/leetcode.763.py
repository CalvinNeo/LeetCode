class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        def move_j(i, j):
            c = S[i]
            while j > i and S[j] != c:
                j -= 1
            # j == i or S[j] == S[i]
            return j
        ans = []
        i = 0
        while i < n:
            j = i
            k = i
            while k <= j:
                newj = move_j(k, n - 1)
                j = max(j, newj)
                k += 1
            ans.append(j - i + 1)
            # print S[i:j+1]
            i = j + 1
        if n - i > 0:
            ans.append(n - i)
        return ans