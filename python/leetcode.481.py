#coding: utf8
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        seq = [1,2,2]
        def get_index(i):
            # 获得位置是i的列表的值
            return seq[i]

        ri = 1 # 读指针
        wi = 2 # 写指针

        while wi < n:
            # 一个循环，ri前进一格
            # wi和ri为上一轮结束后的值
            pv = seq[wi] # 上一个slot是什么数字
            nv = 3 - pv # 这个slot是什么数字
            ri += 1
            nl = seq[ri] # 这一轮长度是多少
            seq.extend([nv] * nl)
            wi += nl
            # print "seq", seq

        return sum([1 if x == 1 else 0 for x in seq[:n]])


sln = Solution()
print sln.magicalString(6)