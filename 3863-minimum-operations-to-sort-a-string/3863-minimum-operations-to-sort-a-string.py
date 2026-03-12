class Solution:
    def minOperations(self, s: str) -> int:
        s = list(s)
        target = sorted(s)
        if s == target: return 0
        s1 = sorted(s[:-1]) + [s[-1]]
        s2 = [s[0]] + sorted(s[1:])
        # print(s1)
        # print(s2)
        if s1 == target or s2 == target: return 1
        s1 = [s1[0]] + sorted(s1[1:])
        s2 = sorted(s2[:-1]) + [s2[-1]]
        # print(s1)
        # print(s2)
        if s1 == target or s2 == target: return 2
        s1 = sorted(s1[:-1]) + [s1[-1]]
        s2 = [s2[0]] + sorted(s2[1:])
        if s1 == target or s2 == target: return 3
        # print(s1)
        # print(s2)
        return -1