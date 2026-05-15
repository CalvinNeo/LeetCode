
# Smallest on the top
class PQ:
    def __init__(self):
        self.a = []

lson = lambda x: x * 2 + 1
rson = lambda x: x * 2 + 2
parent = lambda x: (x - 1) / 2

def has_parent(pq, i):
    return i != 0

def has_lson(pq, i):
    return lson(i) < len(pq.a)

def has_rson(pq, i):
    return rson(i) < len(pq.a)

def swap(pq, i, j):
    pq.a[i], pq.a[j] = pq.a[j], pq.a[i]

def sink(pq):
    if not pq.a:
        return
    i = 0
    while True:
        c = pq.a[i]
        if not has_lson(pq, i):
            break
        if has_rson(pq, i):
            l = pq.a[lson(i)]
            r = pq.a[rson(i)]
            # the bigger, the deeper
            if c > l or c > r:
                if l < r:
                    swap(pq, i, lson(i))
                    i = lson(i)
                else:
                    swap(pq, i, rson(i))
                    i = rson(i)
            else:
                break
        else:
            l = pq.a[lson(i)]
            if c > l:
                swap(pq, i, lson(i))
                i = lson(i)
            else:
                break

def swim(pq):
    i = len(pq.a) - 1
    while True:
        if not has_parent(pq, i):
            break
        c = pq.a[i]
        p = pq.a[parent(i)]
        if c < p:
            swap(pq, i, parent(i))
            i = parent(i)
        else:
            break

def insert(pq, x):
    print "insert", x
    pq.a.append(x)
    swim(pq)
    # print "after insert {}".format(pq.a)

def pop(pq):
    x = pq.a[0]
    n = len(pq.a)
    assert n > 0
    pq.a[0] = pq.a[-1]
    pq.a = pq.a[:n-1]
    sink(pq)
    # if n - 1 > 0:
    #     print "after pop {}".format(pq.a)
    return x

class Solution(object):
    def topKFrequentAC(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in nums:
            if not x in d:
                d[x] = 0
            d[x] += 1
        arr = sorted(list(d.iteritems()), key = lambda x:x[1], reverse = True)
        ans = []
        for i in xrange(k):
            ans.append(arr[i][0])
        return ans

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        

pq = PQ()
insert(pq, 3)
insert(pq, 7)
insert(pq, 8)
insert(pq, 2)
insert(pq, 1)
print "===="
print pop(pq)
print pop(pq)
print pop(pq)
print pop(pq)
print pop(pq)

pq = PQ()
insert(pq, 8)
insert(pq, 1)
print "===="
print pop(pq)
print pop(pq)

pq = PQ()
insert(pq, 1)
insert(pq, 3)
print "===="
print pop(pq)
print pop(pq)

pq = PQ()
insert(pq, 3)
insert(pq, 7)
insert(pq, 8)
insert(pq, 1)
print "===="
print pop(pq)
print pop(pq)
print pop(pq)
print pop(pq)

# sln = Solution()
# print sln.topKFrequent([1,1,1,2,2,3], 2)