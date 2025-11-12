class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = 0
        g = 0

        for num in nums:
            if num == 1:
                ones += 1
            g = gcd(g, num)
            
        if ones > 0:
            return n - ones
        if g > 1:
            return -1

        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i)
                    break

        return min_len + n - 1
