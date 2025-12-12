class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        for i in range(n):
            for j in range(n):
                if j == i: continue
                for k in range(n):
                    if k == i or k == j: continue
                    ans = max(ans, (nums[i] + nums[j]) - nums[k])
        return ans
                    