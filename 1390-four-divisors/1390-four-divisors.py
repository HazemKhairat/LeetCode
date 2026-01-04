class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            arr = set([1, num])
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    arr.add(i)
                    arr.add(num // i)
            if len(arr) == 4:
                ans += sum(arr)
        return ans
                    
        