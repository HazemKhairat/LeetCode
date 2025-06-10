class Solution:
    def maxDifference(self, s: str) -> int:
        diff = 0

        maxOdd = 0
        minEven = float('inf')

        freq = Counter(s)

        for ch, num in freq.items():
            if num % 2 == 0:
                minEven = min(minEven, num)
            else:
                maxOdd = max(maxOdd, num)
        
        diff = maxOdd - minEven

        return diff