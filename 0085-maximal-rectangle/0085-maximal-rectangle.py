class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:  
            return 0

            
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols

        max_area = 0

        for row in matrix:
            for col in range(cols):
                heights[col] = heights[col] + 1 if row[col] == '1' else 0

            n = len(heights)
            for i in range(n):
                for j in range(i, n):
                    min_height = min(heights[i : j + 1])
                    area = (j - i + 1) * min_height
                    max_area = max(max_area, area)

        return max_area
