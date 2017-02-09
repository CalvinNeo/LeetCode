class NFANode:
    def __init__(self, index):
        self.goto = {}
        self.finish = False
        self.index = index
    def add_goto(self, ch, dest):
        self.goto[ch] = dest

class DFANode:
    def __init__(self, nfalist = set()):
        self.goto = {}
        self.nfas = nfalist
        self.nfa_goto = {}
        self.nfa_finish = {}
        self.finish = False
    def add_goto(self, ch, dest):
        self.goto[ch] = dest

class Solution(object):
    def makeNFA(self, p):
        index = 0
        start = NFANode(index)
        cur = start
        i = 0
        while i < len(p):
            index += 1
            nd = NFANode(index)
            if p[i] == '.':                
                if i + 1 < len(p) and p[i + 1] == '*':
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        cur.add_goto(ch, cur)
                    cur.add_goto("", nd)
                    i += 2
                else:
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        cur.add_goto(ch, nd)
                    i += 1
            else:
                if i + 1 < len(p) and p[i + 1] == '*':
                    cur.add_goto(p[i], cur)
                    cur.add_goto("", nd)
                    i += 2
                else:
                    cur.add_goto(p[i], nd)
                    i += 1
            cur = nd
        cur.finish = True
        return start

    def find_all_eps_closure(self, nfa):
        ec = set()
        ec.add(nfa)
        for ch, dest in nfa.goto.iteritems():
            if ch == "":
                ec = ec.union(self.find_all_eps_closure(dest))
        return ec

    def NFA2DFA(self, nfa):
        subsets = []
        dfanodes = []
        ec = self.find_all_eps_closure(nfa)
        # T0
        dfanode = self.add_subset(subsets, dfanodes, ec)
        rrr = self.makeDFANode(subsets, dfanodes, dfanode)
        return rrr

    def add_subset(self, subsets, dfanodes, subset):
        index = None
        dnode = None
        try:
            index = subsets.index(subset)
            dnode = dfanodes[index]
            return dnode
        except ValueError:
            dnode = DFANode(subset)
            subsets.append( subset )
            dfanodes.append( dnode )
            self.makeDFANode(subsets, dfanodes, dnode)
            return dnode

    def makeDFANode(self, subsets, dfanodes, dfanode):
        nfa_goto = {}
        for nfa in dfanode.nfas:
            dfanode.finish = dfanode.finish or nfa.finish
            for ch, dest in nfa.goto.iteritems():
                # nfa --ch--> dest
                if nfa_goto.has_key(ch):
                    nfa_goto[ch].append(dest)
                else:
                    nfa_goto[ch] = [dest]
        for ch in nfa_goto.keys():
            dfanode.nfa_goto[ch] = set()
            for nfa in nfa_goto[ch]:
                dfanode.nfa_goto[ch] = dfanode.nfa_goto[ch].union(self.find_all_eps_closure(nfa))
        for ch, destset in dfanode.nfa_goto.iteritems():
            dnode = self.add_subset(subsets, dfanodes, destset)
            dfanode.goto[ch] = dnode
            #dfanode.goto[ch].finish = dfanode.nfa_finish[ch]
        return dfanode

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        start = self.makeNFA(p)
        start = self.NFA2DFA(start)
        cur = start
        for ch in s:
            if ch in cur.goto.keys():
                cur = cur.goto[ch]
            elif '.' in cur.goto.keys():
                cur = cur.goto['.']
            else:
                return False
        return True if cur.finish else False
sln = Solution()

#print sln.isMatch("aaa","a*a") # true
#print sln.isMatch("aa","a") # false
#print sln.isMatch("ab","ab") # true
#print sln.isMatch("aaa","aa") # false
#print sln.isMatch("aa", "a*") # true
#print sln.isMatch("aa", ".*") # true
#print sln.isMatch("ab", ".*") # true
#print sln.isMatch("aab", "c*a*b") # true
print sln.isMatch("abcccde", "abc*de") # true
print sln.isMatch("abbbc", "a.*c") # true
print sln.isMatch("abcdede", "ab.*de") # true
