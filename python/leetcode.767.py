import Queue
class Solution(object):
    # Need to be constantly optimized
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        if n == 0:
            return ""
        s = list(S)
        d = {i:s.count(i) for i in s}
        class Node(object):
            def __init__(self, x, y):
                self.val = x
                self.count = y
            def __cmp__(self, other):
                return -cmp(self.count, other.count)

        pq = Queue.PriorityQueue()
        dl = list(d.iteritems())
        for (x, y) in dl:
            pq.put(Node(x, y))

        ans = []
        while len(ans) < n:
            nd = pq.get()
            if ans and nd.val == ans[-1]:
                if pq.empty():
                    break
                nd2 = pq.get()
                nd, nd2 = nd2, nd
                pq.put(nd2)

            ans.append(nd.val)
            nd.count -= 1
            if nd.count > 0:
                pq.put(nd)

        if len(ans) < n:
            return ""
        else:
            return ''.join(ans)

sln = Solution()
print sln.reorganizeString("") #
print sln.reorganizeString("aab") # aba
print sln.reorganizeString("aaab") # 
print sln.reorganizeString("a") # a
print sln.reorganizeString("blflxll") # lxlblfl
print sln.reorganizeString("bfrbs") # brbsf
print sln.reorganizeString('ogccckcwmbmxtsbmozli') # cmcmcbolzboxctmgiwks
print sln.reorganizeString("tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao") # 