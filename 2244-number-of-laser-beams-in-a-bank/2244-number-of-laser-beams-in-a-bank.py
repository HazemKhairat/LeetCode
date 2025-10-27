class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        n, m = len(bank), len(bank[0])
        for ch in bank[0]:
            if ch == "1":
                prev += 1

        ans = 0
        for i in range(1, n):
            curr = 0
            for j in range(m):
                if bank[i][j] == "1":
                    curr += 1
            if curr:
                ans += curr * prev
                prev = curr

        return ans
