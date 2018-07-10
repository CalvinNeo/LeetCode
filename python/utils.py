class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def print_tree(root, dep = 0):
    print "{}{}".format("\t"*dep, root.val)
    if root.left != None:
        print_tree(root.left, dep+1)
    if root.right != None:
        print_tree(root.right, dep+1)

def build_tree(n, root, p):
    # change root in-place
    root.val = n[p]
    lson = 2 * p + 1
    rson = 2 * p + 2
    if lson < len(n) and n[lson] != None:
        root.left = TreeNode(0)
        build_tree(n, root.left, lson)
    if rson < len(n) and n[rson] != None:
        root.right = TreeNode(0)
        build_tree(n, root.right, rson)

def make_tree(n):
    N1 = TreeNode(0)
    build_tree(n, N1, 0)
    return N1

null = None
inf = 0x3f3f3f3f

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def make_linked(arr):
    H = ListNode(0)
    C = H
    for x in arr:
        C.next = ListNode(x)
        C = C.next
    return H.next

def print_linked(head):
    while head != None:
        print head.val, " ",
        head = head.next
    print ""

def print_mat(mat):
    n = len(mat)
    if n == 0:
        return 0
    m = len(mat[0])
    for line in mat:
        print ' '.join(map(str, line))


def Dijkstra(dis, vis, m):
    dis = [inf for j in xrange(m)]
    vis = [False for j in xrange(m)]
    dis[0] = 0
    for i in xrange(1, m + 1):
        mark = -1
        mindis = inf
        for j in xrange(1, m + 1):
            if not v[j] and dis[j] < mindis:
                mindis = dis[j]
                mark = j
        v[mark] = 1
        for j in xrange(1, m + 1):
            if not v[j]:
                dis[j] = min(dis[j], dis[mark] + G[mark][j])
    return dis