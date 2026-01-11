class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        r = len(mat)
        c = len(mat[0])

        heights = [0] * c
        n = len(heights)
        max_area = 0
        for row in mat:
            for col in range(c):
                heights[col] = heights[col] + 1 if row[col] == "1" else 0

            for i in range(n):
                for j in range(i, n):
                    min_height = min(heights[i : j + 1])
                    area = (j - i + 1) * min_height
                    max_area = max(max_area, area)
        return max_area
