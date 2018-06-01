import Queue
class Solution(object):
    def findItineraryWA(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = {}
        d = {}
        G["="] = ["JFK"]
        d["="] = 0
        d["JFK"] = 1
        for (f, t) in tickets:
            if not f in G:
                G[f] = []
            if not t in d:
                d[t] = 0
            # Add a path from f to t
            G[f].append(t)
            d[t] += 1

        pq = Queue.PriorityQueue()
        for (k, v) in d.iteritems():
            if v == 0:
                pq.put(k)
        ans = []
        while not pq.empty():
            a = pq.get()
            ans.append(a)
            if a in G:
                for nxt in G[a]:
                    d[nxt] -= 1
                    if d[nxt] <= 0:
                        pq.put(nxt)
        return ans[1:]

    def findItineraryWA2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = {}
        n = len(tickets)
        for (f, t) in tickets:
            if not f in G:
                G[f] = Queue.PriorityQueue()
            # Add a path from f to t
            G[f].put(t)

        ans = []
        cur = "JFK"

        for i in xrange(n):
            ans.append(cur)
            nxt = G[cur].get()
            cur = nxt
        ans.append(cur)
        return ans

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = {}
        n = len(tickets)
        for (i, (f, t)) in enumerate(tickets):
            if not f in G:
                G[f] = []
            G[f].append(i)

        for k in G.keys():
            # sort by related egdes's to
            G[k].sort(key = lambda i: tickets[i][1])

        vis = [0] * n
        self.ans = []
        def dfs(cur, ll):
            # print cur, ll
            if len(ll) == n:
                self.ans = ll + [cur]
                return True
            if cur in G:
                for e in G[cur]:
                    if not vis[e]:
                        vis[e] = 1
                        nxt = tickets[e][1]
                        if dfs(nxt, ll + [cur]):
                            return True
                        vis[e] = 0
            return False
        dfs("JFK", [])
        return self.ans

sln = Solution()
print sln.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
# ["JFK","ATL","JFK","SFO","ATL","SFO"]
print sln.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print sln.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])