class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def findMin(arr):
            res = inf
            idx = -1
            for i in range(len(arr) - 1):
                if arr[i] + arr[i + 1] < res:
                    res = arr[i] + arr[i + 1]
                    idx = i
            return (idx, res)
            
        def isSorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        res = copy.deepcopy(nums)
        ans = 0
    
        while not isSorted(res):
            x, total = findMin(res)
            res = res[:x] + [total] + res[x + 2:]
            ans += 1

        return ans
                
            