class Solution:
    def numOfUnplacedFruits(self, f: List[int], b: List[int]) -> int:
        for i in range(len(f)):
            for j in range(len(b)):
                if f[i] <= b[j]:
                    b[j] = 0
                    f[i] = 0
                    break
        cnt = 0
        for num in f:
            if num != 0:
                cnt += 1
        return cnt
