class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd1 = odd2 = even1 = even2 = 0

        for i in range(1, n + 1):
            if i % 2 == 0:
                even1 += 1
            else:
                odd1 += 1
        for i in range(1, m + 1):
            if i % 2 == 0:
                even2 += 1
            else:
                odd2 += 1
        
        return (even1 * odd2) + (even2 * odd1)