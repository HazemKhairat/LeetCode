class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create dictionary (dic) to store number and it's index
        dic = {}
        for idx, num in enumerate(nums):
            dic[num] = idx

        # if (target - currNum) in dic return [currIdx, dic[(target - currNum)]]
        for i in range(len(nums)):
            use = target - nums[i]
            if use in dic and dic[use] != i:
                return [i, dic[use]]

        return [-1, -1]
