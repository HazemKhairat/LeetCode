class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        ans = 0

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                mid = stack.pop()
                if stack:
                    l = stack[-1]
                    r = i
                    if min(nums[l], nums[r]) > nums[mid]:
                        ans += 1
            
            stack.append(i)
        
        return ans
