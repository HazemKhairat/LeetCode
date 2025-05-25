class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        res = 0
        mid = 0

        for word, num in cnt.items():
            rev = word[::-1]
            if word[0] == word[1]:
                res += num - (num % 2)
                mid |= num % 2
            elif rev in cnt:
                res += min(num, cnt[rev])

        return (res + mid) * 2
