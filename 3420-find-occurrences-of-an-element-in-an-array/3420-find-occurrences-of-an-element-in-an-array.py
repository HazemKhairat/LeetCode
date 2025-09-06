class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        dic = Counter()
        cnt = 1

        for i, num in enumerate(nums):
            if x == num:
                dic[cnt] = i
                cnt += 1

        ans = [-1]  * len(queries)
        for i, q in enumerate(queries):
            if q in dic:
                ans[i] = dic[q]

        return ans
                
        