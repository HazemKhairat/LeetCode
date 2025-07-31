class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            while len(stack) > 0 and num < stack[-1]:
                stack.pop()

            if not stack or num > stack[-1]:
                if num == 0:
                    continue
                ans += 1
                stack.append(num)

        return ans
            
            
                    
        