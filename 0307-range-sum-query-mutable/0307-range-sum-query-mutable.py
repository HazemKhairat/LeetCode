class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * 4 * self.n
        self.buildTree(nums, 0, self.n - 1, 0)

    def buildTree(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return
        mid = (left + right) // 2
        self.buildTree(nums, left, mid, 2 * index + 1)
        self.buildTree(nums, mid + 1, right, 2 * index + 2)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def sumRange(self, left, right, queryL, queryR, index):
        if queryL > right or queryR < left:
            return 0

        if queryL <= left and right <= queryR:
            return self.tree[index]

        mid = (left + right) // 2
        qleft = self.sumRange(left, mid, queryL, queryR, 2 * index + 1)
        qright = self.sumRange(mid + 1, right, queryL, queryR, 2 * index + 2)
        return qleft + qright

    def update(self, left, right, index, pos, val):
        if left == right:
            self.tree[index] = val
            return
        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2 * index + 1, pos, val)
        else:
            self.update(mid + 1, right, 2 * index + 2, pos, val)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(0, self.n - 1, 0, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sumRange(0, self.n - 1, left, right, 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
