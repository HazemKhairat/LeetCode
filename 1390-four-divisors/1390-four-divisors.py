class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if sqrt(num) == int(sqrt(num)):
                continue
            arr = []
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    arr.append(i)
                    arr.append(num // i)
                    if len(arr) > 4:
                        break
            if len(arr) == 4:
                ans += sum(arr)
        return ans
