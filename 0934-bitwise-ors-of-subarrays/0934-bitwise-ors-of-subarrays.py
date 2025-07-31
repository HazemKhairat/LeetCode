class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        curr = {0}
        ans = set()

        for num in arr:
            curr = {num | item for item in curr}
            curr.add(num)
            ans |= curr
        
        return len(ans)


