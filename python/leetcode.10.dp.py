# coding: utf8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = "#" + s
        p = "#" + p
        sl = len(s)
        pl = len(p)

        dp = [[0 for i in xrange(pl + 1)] for j in xrange(sl + 1)]
        # dp[i][j]表示s[0, i]和p[0, j]是否是match的
        # 现对sln.isMatch("", "a*")不是很好处理，主要是一个串的长度为0，导致无法进入for循环
        # 因此，我们对每个串前面都加一个必定能匹配的#

        dp[-1][-1] = 1
        # for i in xrange(pl + 1):
        #     dp[-1][i] = 1
        # for i in xrange(sl + 1):
        #     dp[i][-1] = 1

        for si in xrange(sl):
            for pi in xrange(pl):
                cs = s[si]
                cp = p[pi]
                # print "s[{}] {} p[{}] {}".format(si, s[si], pi, p[pi])
                if cp == ".":
                    # 如果pattern是.，那么肯定是能match当前符号的
                    dp[si][pi] = dp[si - 1][pi - 1]
                elif cp == "*":
                    if p[pi - 1] == ".":
                        # 如果是.，那么可以选择匹配，也可以不匹配
                        flag = 0
                        # 如果选择不匹配
                        flag = dp[si][pi - 2]
                        # 如果选择匹配，走和下面类似的流程
                        if not flag:
                            for i in xrange(si - 1, -1, -1):
                                if dp[i][pi - 2]:
                                    flag = 1
                                    break
                        dp[si][pi] = flag
                    else:
                        need_to_repeat_char = p[pi - 1]
                        # 是否一个字符都匹配不了
                        actual_eps = s[si] != need_to_repeat_char
                        # prev_p是上一个规则
                        prev_p = pi - 2
                        # print "need_to_repeat_char at {} is {} cmp with s[{}] = {}. actual_eps {}, prev_p {}".format(pi - 1, need_to_repeat_char, si, s[si], actual_eps, prev_p)
                        if actual_eps:
                            # 如果实际Match了0次，说明这个规则没用上，就用上面一个规则的结果
                            if prev_p < 0:
                                # 如果上一个规则不存在，就忽略这个规则
                                dp[si][pi] = 1
                            else:
                                # 否则使用上一个规则的结果
                                dp[si][pi] = dp[si][pi - 2]
                        else:
                            # 如果实际Match了1次及以上，那么用上一个结果
                            # print "adopt dp[{}][{}] = {}".format(si - 1, pi, dp[si - 1][pi])

                            if prev_p < 0:
                                # 如果上一个规则不存在，就认为匹配了
                                dp[si][pi] = 1
                            else:
                                # 否则，我们回溯所有的a，看有没有能够匹配规则的？
                                flag = 0
                                # print "Find Prev Rules from s[{}] match p[{}]".format(si, pi - 2)
                                for i in xrange(si, -1, -1):
                                    if s[i] == need_to_repeat_char and dp[i][pi - 2]:
                                        flag = 1
                                        break
                                    elif s[i] != need_to_repeat_char:
                                        flag = dp[i][pi - 2]
                                        break
                                dp[si][pi] = flag

                else:
                    # 如果pattern是一个字母，那么简单比较对应位置是否匹配
                    dp[si][pi] = (cs == cp) and dp[si - 1][pi - 1]
        # print "ans dp[{}][{}] is {}".format(sl - 1, pl - 1, dp[sl - 1][pl - 1])
        return bool(dp[sl - 1][pl - 1])

    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     sl = len(s)
    #     pl = len(p)

    #     dp = [[0 for i in xrange(pl + 1)] for j in xrange(sl + 1)]
    #     # dp[i][j]表示s[0, i)和p[0, j)是否是match的
    #     for si in xrange(sl):
    #         for pi in xrange(pl):


sln = Solution()
print sln.isMatch("a", "a") # T
print sln.isMatch("a", "a*") # T
print sln.isMatch("", "a*") # T
print sln.isMatch("b", "a") # F
print sln.isMatch("b", "a*") # F
print sln.isMatch("aa", "a") # F
print sln.isMatch("aa", "a*") # T
print sln.isMatch("aa", ".*") # T
print sln.isMatch("ab", ".*") # T
print sln.isMatch("", ".*") # T
print sln.isMatch("mississippi", "mis*is*p*.") # F
print sln.isMatch("ipp", "p*") # F
print sln.isMatch("aa", "aa*") # T
