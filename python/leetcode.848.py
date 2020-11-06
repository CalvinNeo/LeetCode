import string
from operator import iadd

def accum(L):
    if len(L)<2: return L
    return accum(L[:-1]) + [sum(L)]

ABC = list('abcdefghijklmnopqrstuvwxyz')
mp = {ABC[i]:i for i in range(len(ABC))}
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shifts.reverse()
        s = accum(shifts)
        s.reverse()
        return ''.join(map(lambda tp: ABC[(mp[tp[0]]+tp[1])%26] , zip(S, s)))