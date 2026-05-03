class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        n = len(s)
        while i < n:
            if s == goal:
                return True

            s = s[1:] + s[0]
            i += 1

        return False
