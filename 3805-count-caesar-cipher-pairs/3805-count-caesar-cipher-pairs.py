class Solution:
    def countPairs(self, words: List[str]) -> int:
        pattern_cnt = Counter()
        total = 0

        for word in words:
            chars = ["0"] * len(word)
            for i in range(1, len(word)):
                chars[i] = str((ord(word[i]) - ord(word[i - 1])) % 26)
            pattern = "".join(chars)
            total += pattern_cnt[pattern]
            pattern_cnt[pattern] += 1

        return total
