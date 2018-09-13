class Solution(object):
    def numBusesToDestinationTLE(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        d = {}
        for bus, rt in enumerate(routes):
            for stop in rt:
                if stop not in d:
                    d[stop] = []
                d[stop].append(bus)

        n = len(routes)
        con = [[] for i in xrange(n)]

        fin = [0] * n
        for stop, lst in d.iteritems():
            m = len(lst)
            for i in xrange(m):
                if stop == T:
                    fin[lst[i]] = 1
                for j in xrange(i + 1, m):
                    con[lst[i]].append(lst[j])
                    con[lst[j]].append(lst[i])

        import Queue
        q = Queue.Queue()

        vis = [0] * n

        if S not in d or T not in d:
            return -1

        for bus in d[S]:
            q.put((bus, 0))

        while not q.empty():
            bus, deep = q.get()
            vis[bus] = 1
            if fin[bus]:
                return deep + 1
            for nxt in con[bus]:
                if not vis[nxt]:
                    q.put((nxt, deep + 1))
        return -1

    def numBusesToDestinationTLE2(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        n = len(routes)
        start = []
        m = 0
        rinfo = {}
        fin = [0] * n
        for i, r in enumerate(routes):
            for s in r:
                m = max(m, s)

                if s not in rinfo:
                    rinfo[s] = []
                rinfo[s].append(i)

                if s == S:
                    start.append(i)
                if s == T:
                    fin[i] = 1

        vis_s = [0] * (m + 1)
        vis_r = {}

        import Queue
        q = Queue.Queue()

        for r in start:
            q.put((S, r, 0))

        while not q.empty():
            s, r, deep = q.get()
            vis_s[s] = 1
            if fin[r]:
                return deep + 1

            # For all stop in this routine
            for ns in routes[r]:
                if not vis_s[ns]:
                    q.put((ns, r, deep))
            vis_r[r] = 1

            # For all routine in this stop
            for nr in rinfo[s]:
                if nr not in vis_r:
                    # print "Swith to routine {} from {} at stop {}".format(nr, r, s)
                    q.put((s, nr, deep + 1))
        return -1

    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        n = len(routes)
        rinfo = {}
        for i, r in enumerate(routes):
            for s in r:
                if s not in rinfo:
                    rinfo[s] = []
                rinfo[s].append(i)

        vis_s = {}
        vis_r = [0] * n

        import Queue
        q = Queue.Queue()
        q.put((S, 0))

        while not q.empty():
            s, deep = q.get()
            vis_s[s] = 1
            if s == T:
                return deep
            for nr in rinfo[s]:
                if not vis_r[nr]:
                    for ns in routes[nr]:
                        if ns not in vis_s:
                            # print "Goto stop {}, deep {}".format(ns, deep)
                            q.put((ns, deep + 1))
                vis_r[nr] = 1
        return -1

# sln = Solution()
# print sln.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)
# print sln.numBusesToDestination([[1, 7], [3, 5]], 5, 5)