class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.bits = [0] * (self.n + 1)
        for i, num in enumerate(nums, 1):
            j = i
            while j <= self.n:
                self.bits[j] += num
                j += j & -j

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i <= self.n:
            self.bits[i] += diff
            i += i & -i

    def sumRange(self, left: int, right: int) -> int:
        def solve(i):
            total = 0
            while i > 0:
                total += self.bits[i]
                i -= i & -i
            return total

        return solve(right + 1) - solve(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
