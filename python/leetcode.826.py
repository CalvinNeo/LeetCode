import bisect
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        n = len(difficulty)
        m = len(worker)

        if n == 0 or m == 0:
            return 0

        sorted_by_difficulty = sorted(zip(difficulty, profit), key = lambda x: x[0])
        most_profit = [0] * n

        for (i, (d, p)) in enumerate(sorted_by_difficulty):
            if i == 0:
                most_profit[i] = p
            else:
                most_profit[i] = max(most_profit[i - 1], p)
        D, P = zip(*sorted_by_difficulty)
        ans = 0
        # print D
        # print P
        for i, w in enumerate(worker):
            # IMPORTANT!! do NOT use bisect_left
            l = bisect.bisect_right(D, w)
            if l >= n:
                l = n - 1
            if D[l] > w:
                l -= 1
            if l >= 0:
                ans += most_profit[l]
            #     print "Woker[{}] = {}, make profit {}, l {}".format(i, w, most_profit[l], l)
            # else:
            #     print "Woker[{}] = {}, DO NOTHING!!!".format(i, w, most_profit[l])
            #     pass

        return ans