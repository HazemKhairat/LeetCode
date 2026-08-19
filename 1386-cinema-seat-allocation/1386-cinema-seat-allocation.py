from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        def factory():
            return [True, True, True]

        dic = defaultdict(factory)

        for r, c in reservedSeats:
            if c == 2 or c == 3:
                dic[r][0] = False
            elif c == 4 or c == 5:
                dic[r][0] = dic[r][1] = False
            elif c == 6 or c == 7:
                dic[r][1] = dic[r][2] = False
            elif c == 8 or c == 9:
                dic[r][2] = False

        # print(dic)

        ans = 0
        for r, li in dic.items():
            ans += max(li[0] + li[2], li[1])

        return ans + ((n - len(dic)) * 2)
