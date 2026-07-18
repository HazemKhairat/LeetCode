class Solution:
    def findGCD(self, nums: List[int]) -> int:

        def gcdIterative(a, b):
            a, b = abs(a), abs(b)
            while b != 0:
                a, b = b, a % b
            return a

        a, b = min(nums), max(nums)

        return gcdIterative(a, b)
