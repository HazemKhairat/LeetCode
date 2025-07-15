class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])

        for row in range(n):
            for col in range(1, m):
                matrix[row][col] += matrix[row][col - 1]

        for col in range(m):
            for row in range(1, n):
                matrix[row][col] += matrix[row - 1][col]
            
        res = 0
        for r1 in range(n):
            for r2 in range(r1, n):
                count = defaultdict(int)
                count[0] = 1
                for c in range(m):
                    curr_sum = matrix[r2][c] - (matrix[r1 - 1][c] if r1 > 0 else 0)
                    diff = curr_sum - target
                    
                    if diff in count:
                        res += count[diff]
                        
                    count[curr_sum] += 1
            
        return res