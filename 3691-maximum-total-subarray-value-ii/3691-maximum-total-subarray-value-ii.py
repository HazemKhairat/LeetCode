class SegmentTree:
    def __init__(self, size, nums):
        self.nums = nums
        self.size = size
        self.mx = [0] * (size * 2)
        self.mn = [0] * (size * 2)
        self.build()

    def build(self):
        n = self.size
        for i in range(n):
            self.mx[i + n] = self.nums[i]
            self.mn[i + n] = self.nums[i]

        for i in range(n - 1, 0, -1):
            self.mx[i] = max(self.mx[i * 2 + 1], self.mx[i * 2])
            self.mn[i] = min(self.mn[i * 2 + 1], self.mn[i * 2])

    def query(self, left, right):
        l = left + self.size
        r = right + self.size
        mini, maxi = inf, -inf
        while l <= r:

            if l % 2 == 1:
                maxi = max(maxi, self.mx[l])
                mini = min(mini, self.mn[l])
                l += 1

            if r % 2 == 0:
                maxi = max(maxi, self.mx[r])
                mini = min(mini, self.mn[r])
                r -= 1

            l //= 2
            r //= 2

        return maxi - mini


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        segTree = SegmentTree(n, nums)

        pq = []
        for l in range(n):
            val = segTree.query(l, n - 1)
            heapq.heappush(pq, (-val, l, n - 1))

        ans = 0
        for i in range(k):
            # print(pq)
            val, l, r = heapq.heappop(pq)
            if l < r:
                newVal = segTree.query(l, r - 1)
                heapq.heappush(pq, (-newVal, l, r - 1))

            ans += -val

        return ans
