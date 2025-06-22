class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []

        i = 0
        tmpstr = ""
        while i < n:
            tmpstr += s[i]
            if len(tmpstr) == k:
                res.append(tmpstr)
                tmpstr = ""
            i += 1

        if len(tmpstr) != 0:
            while len(tmpstr) < k:
                tmpstr += fill
            res.append(tmpstr)

        return res