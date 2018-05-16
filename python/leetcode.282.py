import operator
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if len(num) == 0:
            return []

        ops = [operator.add, operator.sub, operator.mul]
        opstrs = "+-*"
        def find(chs):
            n = len(chs)
            ans = []
            if n == 0:
                return []
            elif n == 1:
                return [(int(chs), chs)]
            else:
                mid = n / 2
                left = chs[0:mid]
                right = chs[mid:]
                l = find(left)
                r = find(right)

                for ll in l:
                    for rr in r:
                        for (op, opstr) in zip(ops, opstrs):
                            t = op(ll[0], rr[0])
                            ans.append((t, "{}{}{}".format(ll[1], opstr, rr[1])))

                        t = eval(ll[1] + rr[1])
                        ans.append((t, "{}{}".format(ll[1], rr[1])))

                return ans

        ans = find(num)
        res = []

        def valid(epr):
            if eval(epr) != target:
                return False
            nn = len(epr)
            for i in xrange(nn - 1):
                if epr[i] in opstrs and i + 2 < nn:
                    if epr[i + 1] == '0' and epr[i + 2] in "1234567890":
                        return False
                if i == 0 and i + 1 < nn:
                    if epr[i] == '0' and epr[i + 1] in "1234567890":
                        return False
            return True

        for (t, equa) in ans:
            if valid(equa):
                res.append(equa)
        return res

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        n = len(num)
        ans = []
        if n == 0:
            return []

        def valid_num(s):
            return s == '0' or (len(s) > 0 and s[0] != '0')

        def dfs(s, cur_sum, cur_prod, str_sum, str_prod):
            if s == "":
                if str_sum and not str_prod and cur_sum == target:
                    # print "append where str_sum = {} and str_prod = {}".format(str_sum, str_prod)
                    ans.append(str_sum)

            # print "dfs of '{}' when str_num = {}, str_prod = {}".format(s, str_sum, str_prod)
            # I can extend sum if there is a current prod
            if str_prod:
                if str_sum:
                    dfs(s, cur_sum + cur_prod, 1, str_sum + "+" + str_prod, "")
                    dfs(s, cur_sum - cur_prod, 1, str_sum + "-" + str_prod, "")
                else:
                    dfs(s, cur_prod, 1, str_prod, "")

            # Or I can always extend prod
            l = len(s)
            for i in xrange(1, l + 1):
                if valid_num(s[0:i]):
                    str_num = s[0:i]
                    cur_num = int(str_num)
                    rest_s = s[i:]

                    # I can extend prod
                    if str_prod:
                        dfs(rest_s, cur_sum, cur_prod * cur_num, str_sum, str_prod + "*" + str_num)
                    else:
                        dfs(rest_s, cur_sum, cur_num, str_sum, str_num)


        dfs(num, 0, 1, "", "")
        # return list(set(ans))
        return ans

sln = Solution()
# print sln.addOperators("13", 3)
print sln.addOperators("123", 6) # ['1+2+3', '1*2*3']
print sln.addOperators("232", 8) # ["2*3+2", "2+3*2"]
print sln.addOperators("105", 5) # ["1*0+5","10-5"]
print sln.addOperators("00", 0) # ["0+0", "0-0", "0*0"]
print sln.addOperators("3456237490", 9191) # []
print sln.addOperators("2147483648", -2147483648) # []
