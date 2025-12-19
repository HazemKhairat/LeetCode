class Solution:
    def minMoves(self, b: List[int]) -> int:
        n = len(b)
        ans = 0
        index = -1
        for i in range(len(b)):
            if b[i] < 0:
                index = i
        if index == -1: return 0
        used = set()
            
        i, j = index - 1, index + 1
        cost = 1
        while len(used) < n - 1:
            i, j = i % n, j % n

            if i not in used:
                used.add(i)
                b[index] += b[i]
                ans += b[i] * cost
                i -= 1
            
            if b[index] >= 0: 
                ans -= b[index] * cost
                break

            if j not in used:
                used.add(j)
                b[index] += b[j]
                ans += b[j] * cost 
                j += 1
                
            if b[index] >= 0:
                ans -= b[index] * cost
                break
            cost += 1
                
        return ans if b[index] >= 0 else -1