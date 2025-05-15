class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        n = len(words)
        maxi = 0
        res = []

        def solve(prev, index, arr):
            nonlocal maxi, res
            if index == n:
                if maxi < len(arr):
                    res = arr
                    maxi = len(arr)
                return

            if prev == -1 or prev != groups[index]:
                arr.append(words[index])
                solve(groups[index], index + 1, arr)
            else:
                solve(prev, index + 1, arr)

        solve(-1, 0, [])
        return res
