class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        res = [ch if not ch.isalpha() else "" for ch in s]
        tmp = []
        for ch in s:
            if ch.isalpha():
                tmp.append(ch)

        for i in range(len(res)):
            if res[i] == "":
                res[i] = tmp.pop()
                
        return "".join(res)
