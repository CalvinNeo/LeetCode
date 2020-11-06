#coding: utf8

class Solution(object):
    def smallestSufficientTeamDFS(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        tot = 0
        skills = {}
        for s in skills:
            if not s in skills:
                skills[s] = 2 ** tot
                tot += 1
        for p in people:
            for s in p:
                if not s in skills:
                    skills[s] = 2 ** tot
                    tot += 1
        def make_skill(p):
            state = 0
            for s in p:
                state = state | skills[s]
            return state

        people_skills = []
        for p in people:
            people_skills.append(make_skill(p))

        dp = {}

        def dfs(s):
            # s表示当前状态
            if s in dp:
                return dp[s]

            dp[s] = []
            for i, p in enumerate(people_skills):
                # 加上p后的新的状态
                ns = s & (~p) & 0xffffffff
                print "s {:x} ns {:x}".format(s, ns)
                if s == ns:
                    # 如果没有变化，那么就没有必要加上去
                    continue
                else:
                    used = [i] + dfs(ns)
                    if len(dp[s]) > len(used):
                        dp[s] = used
            return dp[s]

        start = make_skill(req_skills)
        dfs(start)
        return dp[0]

    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        tot = 0
        skills = {}
        for s in skills:
            if not s in skills:
                skills[s] = 2 ** tot
                tot += 1
        for p in people:
            for s in p:
                if not s in skills:
                    skills[s] = 2 ** tot
                    tot += 1

        def make_skill(p):
            state = 0
            for s in p:
                state = state | skills[s]
            return state

        people_skills = []
        for p in people:
            people_skills.append(make_skill(p))

        dp = {}

        end_state = make_skill(req_skills)
        # print "need {}".format(end_state)
        self.ans = []
        def update_state(s):
            # 尝试从s开始更新其他状态
            if s == end_state:
                if self.ans == [] or len(self.ans) > len(dp[s]):
                    self.ans = dp[s]
                return
            for i, p in enumerate(people_skills):
                if i in dp[s]:
                    # 如果这个人没有被用过，其实也可以不加这个条件
                    continue
                ns = s | p
                if (not ns in dp) or len(dp[s]) + 1 < len(dp[ns]):
                    # print "update from {} to {} by {}".format(s, ns, i)
                    dp[ns] = [i] + dp[s]
                    update_state(ns)
        dp[0] = []
        update_state(0)
        return self.ans


sln = Solution()
print sln.smallestSufficientTeam(req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]])
print sln.smallestSufficientTeam(req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]])