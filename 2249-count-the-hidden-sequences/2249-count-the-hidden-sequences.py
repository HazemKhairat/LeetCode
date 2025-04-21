class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        # original = 3 -4 5 1 -2 lower = -4, upper = 5
        # let x = 1
        # 1 4 0 5 6 4
        # res = lower - min = -4
        # add res to each value = -3 0 -4 1 2 0
        # ans = upper - max + 1 = 5 - 2 + 1 = 4


        arr = [0]
        x , y = 0, 0
        for num in diff:
            curr = arr[-1] + num
            arr.append(curr)
            x = min(x, curr)
            y = max(y, curr)
            if (y - x) > (upper - lower):
                return 0
        
        res = lower - min(arr)

        for i in range(len(arr)):
            arr[i] += res
        
        return upper - max(arr) + 1