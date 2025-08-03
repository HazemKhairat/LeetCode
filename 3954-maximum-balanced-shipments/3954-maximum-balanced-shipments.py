class Solution:
    def maxBalancedShipments(self, w: List[int]) -> int:
        res = 0
        maxi = w[0]
        for i in range(1, len(w)):
            if w[i] >= maxi:
                maxi = w[i]
            else:
                res += 1
                maxi = 0

        return res