class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        n = len(nums)
        for i in range(n):
            dic[nums[i]].append(i)

        ans = inf
        for num, li in dic.items():
            if len(li) >= 3:
                for i in range(len(li) - 2):
                    i, j, k = li[i], li[i + 1], li[i + 2]
                    ans = min(ans, abs(i - j) + abs(j - k) + abs(k - i))
        return ans if ans != inf else -1