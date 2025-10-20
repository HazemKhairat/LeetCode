class Solution:
    def finalValueAfterOperations(self, ops: List[str]) -> int:
        ans = 0

        for x in ops:
            if x[0] == '+' or x[2] == '+':
                ans += 1
            else:
                ans -= 1
        return ans