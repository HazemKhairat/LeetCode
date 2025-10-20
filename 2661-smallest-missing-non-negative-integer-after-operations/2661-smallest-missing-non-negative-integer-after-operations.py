class Solution:
    def findSmallestInteger(self, nums: List[int], val: int) -> int:
        cnt = Counter([num % val for num in nums])
        mex = 0

        while cnt[mex % val] > 0:
            cnt[mex % val] -= 1
            mex += 1

        return mex
