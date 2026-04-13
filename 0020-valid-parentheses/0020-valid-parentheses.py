class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if not stack or ch in mapping.values():
                stack.append(ch)
            else:
                if mapping[ch] != stack.pop():
                    return False

        return len(stack) == 0
