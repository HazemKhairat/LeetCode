class Solution:
    def finalValueAfterOperations(self, ops: List[str]) -> int:
        return sum([1 if op[1] == '+' else -1 for op in ops])