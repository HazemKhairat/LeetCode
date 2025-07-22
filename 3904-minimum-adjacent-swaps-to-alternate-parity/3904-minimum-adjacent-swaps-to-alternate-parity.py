class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = [i for i, num in enumerate(nums) if num % 2 == 1]
        n, m = len(nums), len(ones) * 2

        def countSwaps(start):
            res = 0
            j = 0
            for i in range(start, n, 2):
                res += abs(ones[j] - i)
                j += 1
            return res

        if n == m:
            return min(countSwaps(0), countSwaps(1))
        elif m == n + 1:
            return countSwaps(0)
        elif m == n - 1:
            return countSwaps(1)

        return -1