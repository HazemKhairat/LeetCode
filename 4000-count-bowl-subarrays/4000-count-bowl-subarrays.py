class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            while stack and stack[-1] < num:
                tmp = stack.pop()
                if stack and stack[-1] > tmp:
                    ans += 1  
            stack.append(num)
        
        return ans
