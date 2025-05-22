class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        available_queries = []
        used_queries = []
        operations = 0
        j = 0

        for i in range(len(nums)):
            while j < len(queries) and queries[j][0] == i:
                heappush(available_queries, -queries[j][1])
                j += 1

            nums[i] -= len(used_queries)
            while nums[i] > 0 and available_queries and -available_queries[0] >= i:
                nums[i] -= 1
                heappush(used_queries, -available_queries[0])
                heappop(available_queries)
                operations += 1

            if nums[i] > 0:
                return -1

            while used_queries and used_queries[0] == i:
                heappop(used_queries)

        return len(queries) - operations
