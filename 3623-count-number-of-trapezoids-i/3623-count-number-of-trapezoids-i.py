class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # Count Points -> how many Xs for each Y axis ?
        cnt = Counter()
        for x, y in points:
            cnt[y] += 1

        # Count Lines for each y row from number of points
        # formula: nCr where n is the total number of points 
        # and r how many points we need to create one line which is constant (always 2)
        # final formula nC2 -> (n * (n - 1)) // 2
        rows = []
        for y, numOfPoints in cnt.items():
            lines = (numOfPoints * (numOfPoints - 1)) // 2
            rows.append(lines)

        # count pref multyply faster
        pref = [rows[0]] * len(rows)
        for i in range(1, len(rows)):
            pref[i] = pref[i - 1] + rows[i]

        # Count how many convex quadrilateral 
        # -> multiply number of lines in each row by number of lines  at the other rows
        ans = 0
        for i in range(len(pref)):
            ans += (rows[i] * (pref[-1] - pref[i])) 
            
        return ans % MOD
            

