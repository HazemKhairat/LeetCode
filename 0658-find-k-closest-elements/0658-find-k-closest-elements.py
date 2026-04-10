class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
            
        ans = []
        
        # print(start)
        # print(arr)
        # print(ans)
        
        i, j = r, l
        
        while k:
            if i < 0:
                ans.append(arr[j])
                j += 1
            elif j == len(arr):
                ans.append(arr[i])
                i -= 1
            elif abs(arr[i] - x) <= abs(arr[j] - x):
                ans.append(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1  
            
            k -= 1
        
        ans.sort()
        return ans
        
        