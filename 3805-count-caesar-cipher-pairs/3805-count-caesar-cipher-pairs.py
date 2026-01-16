class Solution:
    def countPairs(self, words: List[str]) -> int:
        pattern_cnt = Counter()
        ans = 0

        for word in words:
            chars = list(word)
            base = ord(chars[0])
            for i in range(len(word)):
                chars[i] = str((ord(chars[i]) - base) % 26)
            pattern = "".join(chars)
            print(pattern)
            ans += pattern_cnt[pattern]
            pattern_cnt[pattern] += 1

        return ans
