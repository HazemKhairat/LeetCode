class Solution:
    def distinctPoints(self, s: str, k: int) -> int:

        pref = [(0, 0)]
        x = y = 0
        for ch in s:
            if ch == "U":
                y += 1
            elif ch == "D":
                y -= 1
            elif ch == "L":
                x -= 1
            elif ch == "R":
                x += 1
            pref.append((x, y))

        ans = set()
        lx, ly = pref[-1][0], pref[-1][1]
        for i in range(len(pref) - k):
            nx = lx - pref[i + k][0] + pref[i][0]
            ny = ly - pref[i + k][1] + pref[i][1]
            ans.add((nx, ny))

        return len(ans)
