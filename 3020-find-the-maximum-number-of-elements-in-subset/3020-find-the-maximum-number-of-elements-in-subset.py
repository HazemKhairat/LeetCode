class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        def solve(num):
            if num == 1:
                return 0
            tmp = int(sqrt(num))
            if (tmp * tmp) != num or cnt[tmp] < 2:
                return 0

            return 2 + solve(tmp)

        for num in nums:
            ans = max(ans, 1 + solve(num))

        ans = max(ans, cnt[1] if cnt[1] % 2 == 1 else cnt[1] - 1)
        return ans
