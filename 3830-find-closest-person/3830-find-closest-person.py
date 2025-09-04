class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        f = abs(z - x)
        s = abs(z - y)

        if f < s:
            return 1
        elif s < f:
            return 2
        return 0