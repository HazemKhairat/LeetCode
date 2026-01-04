class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        used = {}
        for num in nums:
            if num in used:
                ans += used[num]
                continue

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
                used[num] = sum(arr)
                ans += used[num]
        return ans
