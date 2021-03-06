#coding: utf8
import Queue
import collections
class Solution(object):
    def isEscapePossibleTLE(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        blocked_set = set()

        for [fr, to] in blocked:
            blocked_set.add("{},{}".format(fr, to))

        LIM = 1000000
        BFS_BORDER = 210
        REACH = 201

        def bfs(start):
            vis = [[0 for i in xrange(500)] for j in xrange(500)]
            q = Queue.Queue()
            q.put(start)
            def V(x, y):
                return vis[x - start[0]][y - start[1]]
            def SV(x, y, v = 1):
                vis[x - start[0]][y - start[1]] = 1
            def valid(x, y):
                return (-BFS_BORDER <= x - start[0] <= BFS_BORDER) and (-BFS_BORDER <= y - start[1] <= BFS_BORDER) and (0 <= x < LIM) and (0 <= y < LIM)
            def can(x, y):
                return not "{},{}".format(x, y) in blocked_set
            while not q.empty():
                Dx = [0, 0, 1, -1]
                Dy = [1, -1, 0, 0]
                [x, y] = q.get()
                if V(x, y):
                    continue
                SV(x, y)
                if x - start[0] < -REACH or x - start[0] > REACH or y - start[1] < -REACH or y - start[1] > REACH:
                    # 如果能够成功突围
                    # print "REACH {} {} from {}".format(x, y, start)
                    return True
                for (dx, dy) in zip(Dx, Dy):
                    nx = x + dx
                    ny = y + dy
                    # print "nx {} ny {} not V((nx, ny)) {} can((nx, ny)) {}".format(nx, ny, not V((nx, ny)), can((nx, ny)))
                    if valid(nx, ny) and (not V(nx, ny)) and can(nx, ny):
                        # print x, y, V(x, y), nx, ny
                        q.put([nx, ny])
            return False

        can_src = bfs(source)
        # can_src = True
        can_tar = bfs(target)
        # print "can_tar {} can_src {}".format(can_tar, can_src)
        return (can_tar and can_src)

    def isEscapePossible(self, blocked, source, target):
        N=10**6
        bs=set() 
        for b in blocked:
            bs.add(tuple(b))

        def bfs(p):
            q=collections.deque()
            q.append(p)
            seen=set([tuple(p)])
            while q:
                x,y=q.popleft()
                if len(seen)>19900:return 1 # outside
                for nx,ny in ((x-1,y),(x,y-1),(x,y+1),(x+1,y)):
                    if (nx,ny) not in bs and (nx,ny,) not in seen and 0<=nx<N and 0<=ny<N:
                        q.append((nx,ny))
                        seen.add((nx,ny))
            return 0 # inside
        x,y = bfs(source),bfs(target)
        if x ^ y==1:return False
        else:return True

sln = Solution()
print sln.isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]) # F
print sln.isEscapePossible(blocked = [], source = [0,0], target = [999999,999999]) # T
print sln.isEscapePossible([[100059,100063],[100060,100064],[100061,100065],[100062,100066],[100063,100067],[100064,100068],[100065,100069],[100066,100070],[100067,100071],[100068,100072],[100069,100073],[100070,100074],[100071,100075],[100072,100076],[100073,100077],[100074,100078],[100075,100079],[100076,100080],[100077,100081],[100078,100082],[100079,100083],[100080,100082],[100081,100081],[100082,100080],[100083,100079],[100084,100078],[100085,100077],[100086,100076],[100087,100075],[100088,100074],[100089,100073],[100090,100072],[100091,100071],[100092,100070],[100093,100069],[100094,100068],[100095,100067],[100096,100066],[100097,100065],[100098,100064],[100099,100063],[100098,100062],[100097,100061],[100096,100060],[100095,100059],[100094,100058],[100093,100057],[100092,100056],[100091,100055],[100090,100054],[100089,100053],[100088,100052],[100087,100051],[100086,100050],[100085,100049],[100084,100048],[100083,100047],[100082,100046],[100081,100045],[100080,100044],[100079,100043],[100078,100044],[100077,100045],[100076,100046],[100075,100047],[100074,100048],[100073,100049],[100072,100050],[100071,100051],[100070,100052],[100069,100053],[100068,100054],[100067,100055],[100066,100056],[100065,100057],[100064,100058],[100063,100059],[100062,100060],[100061,100061],[100060,100062]],[100079,100063],[999948,999967]) # F
print sln.isEscapePossible([[0,199],[1,198],[2,197],[3,196],[4,195],[5,194],[6,193],[7,192],[8,191],[9,190],[10,189],[11,188],[12,187],[13,186],[14,185],[15,184],[16,183],[17,182],[18,181],[19,180],[20,179],[21,178],[22,177],[23,176],[24,175],[25,174],[26,173],[27,172],[28,171],[29,170],[30,169],[31,168],[32,167],[33,166],[34,165],[35,164],[36,163],[37,162],[38,161],[39,160],[40,159],[41,158],[42,157],[43,156],[44,155],[45,154],[46,153],[47,152],[48,151],[49,150],[50,149],[51,148],[52,147],[53,146],[54,145],[55,144],[56,143],[57,142],[58,141],[59,140],[60,139],[61,138],[62,137],[63,136],[64,135],[65,134],[66,133],[67,132],[68,131],[69,130],[70,129],[71,128],[72,127],[73,126],[74,125],[75,124],[76,123],[77,122],[78,121],[79,120],[80,119],[81,118],[82,117],[83,116],[84,115],[85,114],[86,113],[87,112],[88,111],[89,110],[90,109],[91,108],[92,107],[93,106],[94,105],[95,104],[96,103],[97,102],[98,101],[99,100],[100,99],[101,98],[102,97],[103,96],[104,95],[105,94],[106,93],[107,92],[108,91],[109,90],[110,89],[111,88],[112,87],[113,86],[114,85],[115,84],[116,83],[117,82],[118,81],[119,80],[120,79],[121,78],[122,77],[123,76],[124,75],[125,74],[126,73],[127,72],[128,71],[129,70],[130,69],[131,68],[132,67],[133,66],[134,65],[135,64],[136,63],[137,62],[138,61],[139,60],[140,59],[141,58],[142,57],[143,56],[144,55],[145,54],[146,53],[147,52],[148,51],[149,50],[150,49],[151,48],[152,47],[153,46],[154,45],[155,44],[156,43],[157,42],[158,41],[159,40],[160,39],[161,38],[162,37],[163,36],[164,35],[165,34],[166,33],[167,32],[168,31],[169,30],[170,29],[171,28],[172,27],[173,26],[174,25],[175,24],[176,23],[177,22],[178,21],[179,20],[180,19],[181,18],[182,17],[183,16],[184,15],[185,14],[186,13],[187,12],[188,11],[189,10],[190,9],[191,8],[192,7],[193,6],[194,5],[195,4],[196,3],[197,2],[198,1],[199,0]], [0,0], [200,200]) # F