class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        visited = set()

        def solve(cost, first, second):
            stack = []
            res = 0
            for i in range(len(s)):
                ch = s[i]
                if ch == first and i not in visited:
                    stack.append((ch, i))
                elif ch == second and stack and i not in visited:
                    index = stack.pop()[1]
                    visited.add(index)
                    visited.add(i)
                    res += cost
                elif ch != first and ch != second:
                    stack = []
            return res

        if  y > x:
            ans = solve(y, 'b', 'a')
            ans += solve(x, 'a', 'b')
        else:
            ans = solve(x, 'a', 'b')
            ans += solve(y, 'b', 'a')        
            
        return ans