class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target: return 0
        ans = 1

        n = len(words)
        prev, nxt = (startIndex - 1 + n) % n, (startIndex + 1) % n
        t = len(words) - 1
        
        while t > 0:
            if words[prev] == target or words[nxt] == target:
                return ans
            ans += 1

            prev, nxt = (prev - 1 + n) % n, (nxt + 1) % n

            t -= 2
        
        return -1



