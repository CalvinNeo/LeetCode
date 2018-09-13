# coding: utf8
import bisect
import Queue
class Solution(object):
    def scheduleCourseWA(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        n = len(courses)

        courses.sort(key = lambda x:x[1]-x[0])
        vis = [0] * n
        print courses
        cur = 0
        # [0,cur]区间有课程安排了
        ans = 0
        while 1:
            mi_index = -1
            mi_value = 0
            st = cur + 1
            for i, c in enumerate(courses):
                latest_start = c[1] - c[0] + 1
                if (not vis[i]) and latest_start >= st:
                    ac_end = st + c[0] - 1
                    if mi_index == -1 or ac_end < mi_value:
                        mi_index = i
                        mi_value = ac_end
            if mi_index != -1:
                print "st {}, choose min_index {} = {}".format(st, mi_index, str(courses[mi_index]))
                ans += 1
                cur = mi_value
                vis[mi_index] = 1
            else:
                break
        return ans

    def scheduleCourseWA2(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        n = len(courses)
        if n == 0:
            return 0
        vis = [0] * n
        courses.sort(key = lambda x:x[1]-x[0])
        cur = 0
        for c in courses:
            cur = max(cur, c[1])
        ans = 0
        # 寻找以cur结尾的
        while 1:
            mx_index = -1
            mx_value = 0
            for i, c in enumerate(courses):
                ac_end = min(cur, c[1])
                ac_start = ac_end - c[0] + 1
                if (not vis[i]) and ac_start > 0:
                    if mx_index == -1 or ac_start > mx_value:
                        mx_index = i
                        mx_value = ac_start

            if mx_index != -1:
                print "aced {}, choose mx_index {} = {}".format(ac_end, mx_index, str(courses[mx_index]))
                ans += 1
                cur = mx_value - 1
                vis[mx_index] = 1
            else:
                break
        return ans

    def scheduleCourseMESS(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        n = len(courses)
        if n == 0:
            return 0
        inf = 55555555555555
        dp = [0] * (n + 1)
        courses.sort(cmp = lambda x,y: cmp(x[1], y[1]))
        cur = 0
        for c in courses:
            cur = max(cur, c[1])
        dp[0] = -cur
        for i in xrange(n-1,-1,-1):
            c = courses[i]
            left = bisect.bisect_right(dp, -c[1])
            dp[left] = -(-dp[left-1] - c[1] + 1)
            # print "left {}, dp[left] {}, dp[left-1] {}".format(left, dp[left], dp[left-1])
        ans = 0
        for i in xrange(n - 1, -1, -1):
            if dp[i] < 0:
                ans += 1
        # print dp
        return ans

    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        n = len(courses)
        if n == 0:
            return 0
        courses.sort(key = lambda x:x[1])
        ans = 0
        cur = 0
        pq = Queue.PriorityQueue()

        for i, c in enumerate(courses):
            pq.put(-c[0])
            cur += c[0]
            if cur > c[1]:
                cur -= -pq.get()
        return pq.qsize()

sln = Solution()
# print sln.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) # 3
print sln.scheduleCourse([[1,2],[2,3]]) # 2
# print sln.scheduleCourse([[1,1]]) # 1
# print sln.scheduleCourse([[2,1]]) # 0
# print sln.scheduleCourse([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]) # 5
# print sln.scheduleCourse([[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]) # 4
# print sln.scheduleCourse([[9,14],[7,12],[1,11],[4,7]]) # 3
# print sln.scheduleCourse([[5,5],[4,6],[2,6]]) # 2