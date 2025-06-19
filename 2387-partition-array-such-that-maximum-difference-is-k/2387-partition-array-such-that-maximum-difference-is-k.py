class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mini, maxi = 1000005, -1000005

        cnt = 1
        for i in range(n):
            mini = min(mini, nums[i])
            maxi = max(maxi, nums[i])
            if maxi - mini > k:
                cnt += 1
                mini = nums[i]
                maxi = nums[i]

        return cnt
