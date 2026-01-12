class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0

        for i in range(n - 1):
            x1, y1, x2, y2 = (
                points[i][0],
                points[i][1],
                points[i + 1][0],
                points[i + 1][1],
            )
            ans += max(abs(y2 - y1), abs(x2 - x1))

        return ans
