class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])

        ans = []

        for dig in range(n + m - 1):
            tmp = []

            r = 0 if dig < m else dig - m + 1
            c = dig if dig < m else m - 1

            while r < n and c >= 0:
                tmp.append(mat[r][c])
                r += 1
                c -= 1
            
            if dig % 2 == 0:
                ans.extend(tmp[::-1])
            else:
                ans.extend(tmp)
            
        return ans