class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        def count(dir1, dir2, time):
            return abs(dir1 - dir2) + time * 2

        ans = 0
        north = south = east = west = 0

        for ch in s:
            if ch == "N":
                north += 1
            elif ch == "S":
                south += 1
            elif ch == "E":
                east += 1
            else:
                west += 1
            # print('N is : ', north)
            # print('S is : ', south)
            # print('E is : ', east)
            # print('W is : ', west)
            time1 = min(north, south, k)
            time2 = min(east, west, k - time1)
            # print('time1 : ', time1)
            # print('time2 : ', time2)
            ans = max(ans, count(north, south, time1) + count(east, west, time2))
            # print(ans)

        return ans
