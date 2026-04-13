class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stack = []
        for ch in ops:
            if ch == "C":
                stack.pop()
            elif ch == "D":
                stack.append(stack[-1] * 2)
            elif ch == "+":
                f = stack[-1]
                s = stack[-2]
                stack.append(f + s)
            else:
                stack.append(int(ch))

        return sum(stack)
