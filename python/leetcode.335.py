#coding: utf8

def multiply(v1, v2):  
    return v1.x*v2.y - v2.x*v1.y  
  
  
class Point:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
  
    def __sub__(self, other):  
        return Point(self.x-other.x, self.y-other.y)  
  
class Segment:  
    def __init__(self, point1, point2):  
        self.point1 = point1  
        self.point2 = point2  
  
    def straddle(self, another_segment):  
        """ 
        :param another_segment: 另一条线段 
        :return: 如果另一条线段跨立该线段，返回True；否则返回False 
        """  
        v1 = another_segment.point1 - self.point1  
        v2 = another_segment.point2 - self.point1  
        vm = self.point2 - self.point1  
        if multiply(v1, vm) * multiply(v2, vm) <= 0:  
            return True  
        else:  
            return False  
  

    def quick_judge(self, another_segment):
        a = self.point1
        b = self.point2
        c = another_segment.point1
        d = another_segment.point2
        ymax1 = max(a.y, b.y)
        ymin1 = min(a.y, b.y)
        xmax1 = max(a.x, b.x)
        xmin1 = min(a.x, b.x)
        ymax2 = max(c.y, d.y)
        ymin2 = min(c.y, d.y)
        xmax2 = max(c.x, d.x)
        xmin2 = min(c.x, d.x)
        if ymin1>ymax2 or ymin2>ymax1 or xmin1>xmax2 or xmin2>xmax1:
            return False
        return True

    def is_cross(self, another_segment):  
        """ 
        :param another_segment: 另一条线段 
        :return: 如果两条线段相互跨立，则相交；否则不相交 
        """  
        if self.straddle(another_segment) and another_segment.straddle(self):  
            return self.quick_judge(another_segment)  
        else:  
            return False  

def cross(l1, l2):
    [x1, y1, x2, y2] = l1
    [x3, y3, x4, y4] = l2
    # print "l1", l1
    # print "l2", l2
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)
    s1 = Segment(p1, p2)
    s2 = Segment(p3, p4)
    # print "is_cross", s1.is_cross(s2)
    return s1.is_cross(s2)

class Solution(object):
    def isSelfCrossing(self, lst):
        """
        :type lst: List[int]
        :rtype: bool
        """
        slots = [None] * 6
        px = 0
        py = 0
        delta = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        for i, dist in enumerate(lst):
            slot_id = i % 6
            delta_id = i % 4
            nx = px + delta[delta_id][0] * dist
            ny = py + delta[delta_id][1] * dist
            # print "px {} py {} nx {} ny {}".format(px, py, nx, ny)
            slots[slot_id] = [px, py, nx, ny]
            # print "slots[{}] = {}".format(i, slots)
            if (not slots[(slot_id - 3) % 6] is None) and cross(slots[slot_id], slots[(slot_id - 3) % 6]):
                return True
            if (not slots[(slot_id - 4) % 6] is None) and cross(slots[slot_id], slots[(slot_id - 4) % 6]):
                return True
            if (not slots[(slot_id - 5) % 6] is None) and cross(slots[slot_id], slots[(slot_id - 5) % 6]):
                return True
            px = nx
            py = ny
        return False

sln = Solution()
print sln.isSelfCrossing([2,1,1,2]) # T
print sln.isSelfCrossing([1,2,3,4]) # F
print sln.isSelfCrossing([1,1,1,1]) # T
print sln.isSelfCrossing([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1]) # F
# print cross([-2, -8, -2, -4], [-2, -2, -2, 2])