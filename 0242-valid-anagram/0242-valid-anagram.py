class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        - Sort s and t strings 
        - if s == t then True else False
        """
        s, t = list(s), list(t)
        s.sort()
        t.sort()

        return s == t