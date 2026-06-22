class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        new_words = []
        cnt = Counter(letters)

        for word in words:
            ok = True
            for ch in word:
                if ch not in cnt:
                    ok = False
                    break
            if ok:
                new_words.append(word)

        def solve(idx, total):
            if idx == len(new_words):
                return total

            new_score = 0
            ans = 0
            ok = True
            cnt1 = Counter(new_words[idx])

            for ch in new_words[idx]:
                if cnt[ch] < cnt1[ch]:
                    ok = False
                    break

            if ok:
                for ch in new_words[idx]:
                    cnt[ch] -= 1
                    i = ord(ch) - ord("a")
                    new_score += score[i]

                ans = max(ans, solve(idx + 1, total + new_score))

                for ch in new_words[idx]:
                    cnt[ch] += 1

            ans = max(ans, solve(idx + 1, total))
            return ans

        return solve(0, 0)
