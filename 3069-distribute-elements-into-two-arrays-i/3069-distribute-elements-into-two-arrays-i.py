class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        n = len(nums) - 2
        i = 2
        while n:
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i]) # 5
            else:
                arr2.append(nums[i]) # 4 
            i += 1
            n -= 1

        return arr1 + arr2
            