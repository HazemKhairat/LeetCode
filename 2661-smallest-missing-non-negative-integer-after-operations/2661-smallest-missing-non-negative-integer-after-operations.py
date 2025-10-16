class Solution:
    def findSmallestInteger(self, nums: List[int], v: int) -> int:

        cnt = Counter()
        for num in nums:
            cnt[num % v] += 1

        mex = 0
        while cnt[mex % v] > 0:
            cnt[mex % v] -= 1
            mex += 1

        return mex
