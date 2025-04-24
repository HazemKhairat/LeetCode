class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key=lambda x: x[1])
        # print(pairs)
        memo = [-1] * n

        def solve(index, prev):
            if index == n:
                return 0

            if memo[index] != -1:
                return memo[index]

            take, skip = 0, 0
            if prev == -1 or pairs[index][0] > pairs[prev][1]:
                take = 1 + solve(index + 1, index)
            skip = solve(index + 1, prev)
            # print("take: ", take)
            # print("skip: ", skip)
            # print(pairs[index])
            memo[index] = max(take, skip)
            return memo[index]

        return solve(0, -1)
