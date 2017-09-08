# class Solution(object):
#     def isScramble(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         import sys
#         m1 = [0] * 256
#         m2 = [0] * 256
#         length = len(s1)
#         for i in xrange(length):
#             m1[ord(s1[i])] += 1
#             m2[ord(s2[i])] += 1
#         for i in xrange(32, 256):
#             if m1[i] != m2[i]:
#                 return False

#         if len(s1) != len(s2) :
#             print "error", s1, s2
#             sys.exit()

#         if len(s1) <= 1:
#             return True

#         for split in xrange(1, length):
#             cl = lambda lst: {x:lst.count(x) for x in lst}
#             l1, r1 = s1[0:split], s1[split:]
#             l2, r2 = s2[0:split], s2[split:]
#             ml1, mr1, ml2, mr2 = cl(l1), cl(r1), cl(l2), cl(r2)
#             print "split", split, "maps",  ml1, mr1, ml2, mr2
#             if cmp(ml1, ml2) == 0:
#                 print "hit1", l1, r1, l2, r2
#                 t1 = self.isScramble(l1, l2)
#                 t2 = self.isScramble(r1, r2)
#                 print "t1", t1, "t2", t2, r1, r2
#                 if t1 and t2:
#                     print "true1"
#                     return True
#             elif cmp(ml1, mr2) == 0:
#                 print "hit2", l1, r1, l2, r2
#                 if self.isScramble(l1, r2) and self.isScramble(r1, l2):
#                     print "true2"
#                     return True
        
#         return False


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        import sys
        if len(s1) != len(s2) :
            print "error", s1, s2
            sys.exit()

        length = len(s1)
        if length <= 1 and s1 == s2:
            return True

        for split in xrange(1, length):
            cl = lambda lst: {x : lst.count(x) for x in lst}
            l1, r1 = s1[0:split], s1[split:]
            ml1, mr1 = cl(l1), cl(r1)

            l2, r2 = s2[0:split], s2[split:]
            ml2, mr2 = cl(l2), cl(r2)
            # print "split", split, "maps",  ml1, mr1, ml2, mr2
            if cmp(ml1, ml2) == 0:
                # print "hit1", l1, r1, l2, r2
                t1 = self.isScramble(l1, l2)
                t2 = self.isScramble(r1, r2)
                # print "t1", t1, "t2", t2, r1, r2
                if t1 and t2:
                    # print "true1"
                    return True

            l2, r2 = s2[0:length-split], s2[length-split:]
            ml2, mr2 = cl(l2), cl(r2)
            if cmp(ml1, mr2) == 0:
                # print "hit2", l1, r1, l2, r2
                if self.isScramble(l1, r2) and self.isScramble(r1, l2):
                    # print "true2"
                    return True
        
        return False


sln = Solution()
print sln.isScramble("abcd", "cdab")
print sln.isScramble("abcd", "bdac")
print sln.isScramble("great", "rgtae")
print sln.isScramble("eat", "tae")
print sln.isScramble("a", "b")
print sln.isScramble("ab", "ba")

