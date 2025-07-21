class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s

        res = ""
        cnt = Counter()
        cnt[s[0]] += 1
        for i in range(1, len(s)):
            if s[i] not in cnt:
                if cnt[s[i - 1]] >= 2:
                    res += s[i - 1] + s[i - 1]
                    cnt.pop(s[i - 1])
                else:
                    res += s[i - 1]
                    cnt.pop(s[i - 1])
            cnt[s[i]] += 1
        first_key = next(iter(cnt))

        if cnt[first_key] >= 2:
            res += first_key + first_key
        else:
            res += first_key

        return res

 
        