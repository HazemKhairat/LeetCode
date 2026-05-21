class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        def get_all_prefixes(arr):
            st = set()
            for num in arr:
                while num:
                    st.add(num)
                    num //= 10
            return st

        st = get_all_prefixes(arr1)

        ans = 0
        for num in arr2:
            while num:
                if num in st:
                    ans = max(ans, len(str(num)))
                num //= 10

        return ans
