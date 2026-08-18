class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        if k == len(nums):
            return max(nums)

        count = [0] * 51
        for i in range(len(nums)):
            count[nums[i]] += 1

        if k == 1:
            for i in range(50, -1, -1):
                if count[i] == 1:
                    return i
            return -1

        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])
        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans
