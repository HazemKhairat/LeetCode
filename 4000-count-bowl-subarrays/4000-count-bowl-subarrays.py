class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = []

        for num in nums:
            while stack and stack[-1] < num:
                stack.pop()
                if stack: ans += 1
            
            if not stack or stack[-1] > num:
                stack.append(num)
        
        return ans