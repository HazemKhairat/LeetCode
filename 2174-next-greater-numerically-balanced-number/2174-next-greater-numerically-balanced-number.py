class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while i < 10**7:
            tmp = i
            cnt = Counter()
            while tmp:
                cnt[tmp % 10] += 1
                tmp //= 10
            ok = True
            for key, val in cnt.items():
                if key != val:
                    ok = False
                    break
            if ok:
                print(cnt)
                return i
            i += 1

        return i
