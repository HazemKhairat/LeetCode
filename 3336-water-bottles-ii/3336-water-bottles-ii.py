class Solution:
    def maxBottlesDrunk(self, nb: int, ne: int) -> int:
        emp = 0
        ans = 0

        while True:
            if emp < ne:
                ans += nb
                emp += nb
                nb = 0
                if emp < ne:
                    break
            else:
                nb += 1
                emp -= ne
                ne += 1
                

        return ans
