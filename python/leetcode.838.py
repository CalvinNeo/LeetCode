# coding: utf8
class Solution(object):
    def pushDominoesNO(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        l = [0] * n
        r = [0] * n
        for i in xrange(n):
            self_condition = 1 if dominoes[i] == 'L' else 0
            if i == 0:
                l[i] = self_condition
            else:
                l[i] = l[i - 1] + self_condition

        for i in xrange(n - 1, -1, -1):
            self_condition = 1 if dominoes[i] == 'R' else 0
            if i == n - 1:
                r[i] = self_condition
            else:
                r[i] = r[i + 1] + self_condition

        force = [0] * n
        ans = ["."] * n
        for i in xrange(n):
            self_condition = 1 if dominoes[i] == 'L' else -1 if dominoes[i] == 'R' else 0
            to_left = self_condition
            if i > 0:
                to_left += force[i - 1]
            to_right = self_condition
            if i < n - 1:
                to_right += force[i + 1]
            force[i] = to_left + to_right
            if force[i] > 0:
                ans[i] = 'L'
            elif force[i] < 0:
                ans[i] = 'R'
        return ''.join(ans)

    def pushDominoesWA(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        l = [0] * n
        r = [0] * n

        for i in xrange(n - 1, -1, -1):
            if i == n - 1:
                if dominoes[i] == "L":
                    l[i] = 1
            else:
                if dominoes[i] == '.':
                    if dominoes[i + 1] == '.' and l[i + 1] > 0:
                        l[i] = l[i + 1] + 1
                    elif dominoes[i + 1] == 'L':
                        l[i] = l[i + 1] + 1
                elif dominoes[i] == 'L':
                    l[i] = 1

        for i in xrange(n):
            if i == 0:
                if dominoes[i] == "R":
                    r[i] = 1
            else:
                if dominoes[i] == 'R':
                    r[i] = 1
                elif dominoes[i] == '.':
                    if dominoes[i - 1] == '.' and r[i - 1] > 0:
                        r[i] = r[i - 1] + 1
                    elif dominoes[i - 1] == 'R':
                        r[i] = r[i - 1] + 1

        ans = ["."] * n
        for i in xrange(n):
            if l[i] > r[i]:
                ans[i] = "L"
            elif l[i] < r[i]:
                ans[i] = "R"
        print l
        print r
        print ans
        print [x - y for (x, y) in zip(l, r)]
        return ''.join(ans)

    def pushDominoes(self, dominoes):
        n = len(dominoes)
        inf = 555555555
        ans = ["."] * n
        close_l_on_left = [-inf] * n
        close_l_on_right = [inf] * n
        close_r_on_left = [-inf] * n
        close_r_on_right = [inf] * n
        
        for i in xrange(n):
            if dominoes[i] == 'L':
                close_l_on_left[i] = i
                close_l_on_right[i] = i
            elif dominoes[i] == 'R':
                close_r_on_left[i] = i
                close_r_on_right[i] = i

        for i in xrange(1, n):
            if dominoes[i] != 'L':
                close_l_on_left[i] = close_l_on_left[i - 1]
            if dominoes[i] != 'R':
                close_r_on_left[i] = close_r_on_left[i - 1]

        for i in xrange(n - 2, -1, -1):
            if dominoes[i] != 'L':
                close_l_on_right[i] = close_l_on_right[i + 1]
            if dominoes[i] != 'R':
                close_r_on_right[i] = close_r_on_right[i + 1]

        for i in xrange(n):
            if dominoes[i] in 'LR':
                ans[i] = dominoes[i]
                continue
            l = close_r_on_left[i] # 从左往右倒
            r = close_l_on_right[i] # 从右往左倒
            to_left = i - l
            to_right = r - i
            lb = close_l_on_left[i] # 从左往左倒
            rb = close_r_on_right[i] # 从右往右倒
            # print "{} = {}: leftD {} rightD {}, l {}, r {}, leftBar {} rightBar {}".format(i, dominoes[i], to_left, to_right, l, r, lb, rb)
            # 可以倒向左边
            can_to_left = (not rb < r) and r != inf
            # 可以倒向右边
            can_to_right = (not lb > l) and l != -inf
            # 从右向左
            # print can_to_left, can_to_right
            if can_to_left and (not can_to_right):
                ans[i] = 'L'
            elif (not can_to_left) and can_to_right:
                ans[i] = 'R'
            elif to_left == to_right:
                pass
            elif to_left > to_right and can_to_left and can_to_right:
                ans[i] = "L"
            # 从左向右
            elif to_left < to_right and can_to_left and can_to_right:
                ans[i] = "R"
        # print close_l_on_right
        # print close_r_on_left
        return "".join(ans)

sln = Solution()
print sln.pushDominoes(".L.R...LR..L..")
print sln.pushDominoes("RR.L")
print sln.pushDominoes("RL")
print sln.pushDominoes("..R..")
print sln.pushDominoes("L.")
print sln.pushDominoes("L.....RR.RL.....L.R.")
print sln.pushDominoes("RLLL..LR....LL......LLR.RL...RRL..........R..L....RR.R..L.LR.L...L..LL.R.R.L.RR.....LRL.L.LL..LRR.L.")
