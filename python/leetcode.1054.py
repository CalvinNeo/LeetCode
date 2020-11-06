from collections import Counter
import Queue
from Queue import PriorityQueue

class Solution(object):
    def rearrangeBarcodesWA(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        arr = sorted(barcodes)
        kva = []

        for a in arr:
            if not kva or a != kva[-1][0]:
                kva.append((a, 0))
            else:
                kva.append((a, kva[-1][1] + 1))

        sa = sorted(kva, cmp=lambda x,y: cmp(x[0],y[0]) if x[1] == y[1] else cmp(x[1],y[1]))
        return [x[0] for x in sa]

    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        c = dict(Counter(barcodes))
        # ck = [x[0] for x in sorted(c.iteritems(), key=lambda x:x[1])]
        q = PriorityQueue()
        for (v, cc) in c.iteritems():
            q.put((-cc, v))

        ans = []
        no_use = None
        while q.qsize() > 0:
            (nc, v) = q.get()
            cc = -nc
            ans.append(v)
            cc -= 1
            if not no_use is None:
                q.put(no_use)
            if cc > 0:
                no_use = (-cc, v)
            else:
                no_use = None
                
        return ans

sln = Solution()
print sln.rearrangeBarcodes([1,1,1,2,2,2])
print sln.rearrangeBarcodes([1,1,1,1,2,2,3,3])