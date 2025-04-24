class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        # print(pairs)
        memo = [[-1] * n for _ in range(n)]

        def solve(index, prev):
            if index == n:
                return 0

            if memo[index][prev] != -1:
                return memo[index][prev]

            take, skip = 0, 0
            if prev == -1 or pairs[index][0] > pairs[prev][1]:
                take = 1 + solve(index + 1, index)
            skip = solve(index + 1, prev)
            # print("take: ", take)
            # print("skip: ", skip)
            # print(pairs[index])
            memo[index][prev] = max(take, skip)
            return memo[index][prev]

        return solve(0, -1)
