class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0] * (5 * self.n)
        def build(l, r, root):
            mid = (l + r) / 2
            if l == r:
                self.tree[root] = nums[l]
            else:
                self.tree[root] = build(l, mid, root * 2 + 1) + build(mid + 1, r, root * 2 + 2)
            return self.tree[root]
        if self.n == 0:
            return
        build(0, self.n - 1, 0)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def upd(index, delta, l, r, root):
            if l <= index <= r:
                self.tree[root] += delta
            if index < l or index > r:
                return
            if l == r:
                return
            mid = (l + r) / 2
            if index <= mid:
                upd(index, delta, l, mid, root * 2 + 1)
            elif index > mid:
                upd(index, delta, mid + 1, r, root * 2 + 2)

        ori = self.sumRange(i, i)
        upd(i, val - ori, 0, self.n - 1, 0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def sea(fr, to, l, r, root):
            if l >= fr and r <= to:
                return self.tree[root]
            if l > to or r < fr:
                return 0

            mid = (l + r) / 2
            return sea(fr, to, l, mid, root * 2 + 1) + sea(fr, to, mid + 1, r, root * 2 + 2)
        return sea(i, j, 0, self.n - 1, 0)

nums = [1,3,5]
obj = NumArray(nums)
print obj.sumRange(0,2)
obj.update(1,2)
print obj.sumRange(0,2)

nums = []
obj = NumArray(nums)

nums = [0,9,5,7,3]
obj = NumArray(nums)
print obj.sumRange(1,2)
obj.update(1,7)
print obj.sumRange(1,2)
obj.update(0,8)
print obj.sumRange(1,2)
