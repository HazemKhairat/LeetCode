class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        pref = [(0, 0)]
        x, y = 0, 0
        for ch in s:
            if ch == "L":
                x -= 1
            elif ch == "R":
                x += 1
            elif ch == "U":
                y += 1
            elif ch == "D":
                y -= 1
            pref.append((x, y))

        n = len(pref)
        total = pref[-1]
        dist_points = set()
        for i in range(n - k):
            X = pref[i][0] + (total[0] - pref[i + k][0])
            Y = pref[i][1] + (total[1] - pref[i + k][1])
            dist_points.add((X, Y))

        return len(dist_points)
