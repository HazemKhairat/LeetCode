import math

class SqrtDecomposition:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.block_size = int(math.sqrt(self.n))
        blocks_nums = (self.n + self.block_size - 1) // self.block_size
        self.blocks = [0] * blocks_nums
        for i in range(self.n):
            block_index = i // self.block_size
            self.blocks[block_index] += nums[i]

    def query(self, l, r):
        ans = 0
        while l % self.block_size != 0 and l <= r:
            ans += self.nums[l]
            l += 1

        while l + self.block_size - 1 <= r:
            block_index = l // self.block_size
            ans += self.blocks[block_index]
            l += self.block_size

        while l <= r:
            ans += self.nums[l]
            l += 1

        return ans

    def update(self, idx, val):
        block_index = idx // self.block_size
        diff = val - self.nums[idx]
        self.nums[idx] = val
        self.blocks[block_index] += diff


class NumArray:

    def __init__(self, nums: List[int]):
        self.sq_d = SqrtDecomposition(nums)

    def update(self, index: int, val: int) -> None:
        self.sq_d.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sq_d.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
