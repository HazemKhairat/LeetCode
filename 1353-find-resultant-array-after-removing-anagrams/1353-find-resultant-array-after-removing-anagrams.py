class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i, j = 0, 1
        n = len(words)
        ans = []
        while j <= n:
            ans.append(words[i])
            while j < n and sorted(words[i]) == sorted(words[j]):
                j += 1
            i = j
            j += 1
        
        return ans
