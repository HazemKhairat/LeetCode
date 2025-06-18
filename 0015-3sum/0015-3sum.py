class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []
        for index in range(n):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            i, j = index + 1, n - 1
            while i < j:
                sum = nums[index] + nums[i] + nums[j]
                if sum < 0:
                    i += 1
                elif sum > 0:
                    j -= 1
                else:
                    res.append([nums[index], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1

                    i += 1
                    j -= 1

        return res
