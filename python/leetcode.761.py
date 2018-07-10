def fch(s, ch):
    try:
        return s.index(ch)
    except ValueError as e:
        return None

def L(s, i, j):
    if i < j:
        return s[i:j]
    return ""

class Solution(object):
    def makeLargestSpecialWA(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        if n == 0:
            return ""
        front0 = S.index('0')
        # The beginning can't be 0
        front1 = front0 - 1
        length = 1
        def find_swap(cnt):
            st1 = front0 + cnt
            while st1 < n:
                while st1 < n and S[st1] == '0':
                    st1 += 1
                i = st1
                while i < n and S[i] == '1':
                    i += 1
                if i - st1 <= cnt:
                    st1 = i
                    continue
                st0 = i
                while st0 < n and S[st0] == '1':
                    st0 += 1
                while i < n and S[i] == '0':
                    i += 1
                if i - st0 > cnt:
                    return st1, cnt * 2 + 2
                st1 = i
            return None, None

        swap1, swaplen = None, None
        while 1:
            if not (front0 - length + 1 >= 0 and front1 + length - 1 < n):
                length -= 1
                break
            if not (S[front0-length+1:front0+1].count('0') == length and S[front1:front1+length].count('1') == length):
                length -= 1
                break
            # front exists
            a, b = find_swap(length)
            if a != None:
                swap1, swaplen = a, b
                length += 1
            else:
                length -= 1
                break

        if swap1 == None:
            # print "Fail", front0+1
            return S[:front0+1] + self.makeLargestSpecial(S[front0+1:])
        else:
            # [st1, ed1)
            st1 = front1-length+1
            ed1 = st1+length*2
            st2 = swap1
            ed2 = swap1+swaplen
            # print "front1 {}, st1 {}, length {}".format(front1, st1, length)
            # print "swap [{},{}]={} with [{},{}]={}".format(st1, ed1, ''.join(arr[st1:ed1+1]), st2, ed2, ''.join(arr[st2:ed2+1]))
            # print st1, ed1, st2, ed2
            ns = L(S, 0, st1) + L(S, st2, ed2) + L(S, ed1, st2) + L(S, st1, ed1) + L(S, ed2, n)
            # print S[:st1] , S[st2:ed2] , S[ed1:st2] , S[st1:ed1] , S[ed2:]
            # print "Succeed", ns, "front =", ns[:front1+swaplen], "next =", ns[front1+swaplen:]
            return ns[:front1+swaplen] + self.makeLargestSpecial(ns[front1+swaplen:])

    def makeLargestSpecialWA2(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        if n == 0:
            return ""
        front0 = S.index('0')
        i = front0
        while i < n and S[i] == '0':
            i += 1
        cnt = i - front0
        front1 = i
        while front1 < n:
            while front1 < n and S[front1] == '0':
                front1 += 1
            i = front1
            while i < n and S[i] == '1':
                i += 1
            if i - front1 >= cnt:
                # Find a FRONT
                break
            else:
                front1 = i
        if front1 != n:
            # Find a FRONT
            rear1 = front1 + cnt
            while rear1 < n and S[rear1] == '0':
                rear1 += 1
            i = rear1
            while i < n and S[i] == '1':
                i += 1
            if i - rear1 >= cnt:
                # We can find enough 1
                end1 = i
                cnt2 = i - rear1
                rear0 = i
                while rear0 < n:
                    while rear0 < n and S[rear0] == '1':
                        rear0 += 1
                    i = rear0
                    while i < n and S[i] == '0':
                        i += 1
                    if i - rear0 >= cnt:
                        # We find a swap
                        break
                    else:
                        rear0 = i
                cnt2 = min(i - rear0, cnt2)
                st1 = front0
                ed1 = front0 + cnt * 2
                st2 = end1 - cnt2
                ed2 = end1 + cnt2
                ns = L(S, 0, st1) + L(S, st2, ed2)
                already = len(ns)
                ns += L(S, ed1, st2) + L(S, st1, ed1) + L(S, ed2, n)
                # print "cnt2", cnt2, "ed1 {}, st2 {}, ed2 {}".format(ed1, st2, ed2)
                # print "S[:st1] {}, S[st1:ed1] {}, S[ed1:st2] {}, S[st2:ed2] {}, S[ed2:] {}".format(S[:st1], S[st1:ed1], S[ed1:st2], S[st2:ed2], S[ed2:])
                # print "ns", ns
                return ns[:already] + self.makeLargestSpecial(ns[already:])
            else:
                return S[:i] + self.makeLargestSpecial(S[i:])
        else:
            # Can't find a FRONT
            return S[:i] + self.makeLargestSpecial(S[i:])

sln = Solution()
print sln.makeLargestSpecial("10") # 10
print sln.makeLargestSpecial("1100") # 1100
print sln.makeLargestSpecial("1010") # 1010
print sln.makeLargestSpecial("100") # 10
print sln.makeLargestSpecial("11011000") # 11100100
print sln.makeLargestSpecial("110110100100") # 111010010100
