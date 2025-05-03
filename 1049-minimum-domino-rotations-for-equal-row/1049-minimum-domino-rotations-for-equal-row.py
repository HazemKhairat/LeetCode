class Solution:

    def minDominoRotations(self, t: List[int], b: List[int]) -> int:
        x = t[0]
        y = b[0]
        cntX = cntY = 0
        cntX2, cntY2 = 0, 0
        for i in range(len(t)):
            if x != t[i] and x != b[i]:
                cntX = float("inf")
                cntX2 = float("inf")
            if y != t[i] and y != b[i]:
                cntY = float("inf")
                cntY2 = float("inf")

        if cntX == cntY == float("inf"):
            return -1

        for i in range(len(t)):
            if x != t[i]:
                cntX += 1
            if y != b[i]:
                cntY += 1

        for i in range(len(t)):
            if x != b[i]:
                cntX2 += 1
            if y != t[i]:
                cntY2 += 1

        return min(min(cntY, cntY2), min(cntX2, cntX))
