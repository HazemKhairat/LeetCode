class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        ans = 0

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
                if stack:
                    ans += 1

            stack.append(i)

        return ans
