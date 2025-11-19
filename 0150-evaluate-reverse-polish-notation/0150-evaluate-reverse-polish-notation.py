class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in ["+", "-", "*", "/"]:
                stack.append(int(item))
            else:
                x = stack.pop()
                y = stack.pop()
                if item == "+":
                    y += x
                elif item == "-":
                    y -= x
                elif item == "*":
                    y *= x
                else:
                    y = int(y / x)
                stack.append(y)

        return stack[-1]
