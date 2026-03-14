class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:

        n = len(nums)
        mini, maxi = min(nums), max(nums)

        def helper(start):  # 0 or 1
            arr = nums[::]
            ans = 0
            for i in range(n):
                if (arr[i] % 2) != start:
                    ans += 1
                    if arr[i] == mini:
                        arr[i] += 1
                    elif arr[i] == maxi:
                        arr[i] -= 1
                start ^= 1
            return [ans, max(arr) - min(arr)]

        return min(helper(0), helper(1))
