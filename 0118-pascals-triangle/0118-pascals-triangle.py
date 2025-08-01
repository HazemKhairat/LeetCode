class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = [ [1] ]

        for row in range(1, n):
            arr = [1]
            for i in range(len(res[row - 1]) - 1):
                arr.append(res[row - 1][i] + res[row - 1][i + 1])
            arr.append(1)
            res.append(arr)
        
        return res
