class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for ch in moves:
            if ch == 'U':
                y += 1
            elif ch == 'D':
                y -= 1
            elif ch == 'L':
                x -= 1
            else:
                x += 1
        
        return (x, y) == (0, 0)