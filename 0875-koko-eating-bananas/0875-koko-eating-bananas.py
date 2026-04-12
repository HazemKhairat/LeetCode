class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            total = 0
            for i in range(len(piles)):
                total += ceil(piles[i] / mid)

            if total == h:
                return mid
            elif total > h:
                l = mid + 1
            else:
                r = mid - 1

        return l
