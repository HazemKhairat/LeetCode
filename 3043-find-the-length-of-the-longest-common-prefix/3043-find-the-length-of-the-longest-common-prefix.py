class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        def get_all_prefixes(arr):
            st = set()
            for num in arr:
                s = str(num)
                for i in range(len(s)):
                    st.add(s[: i + 1])
            return st

        st = get_all_prefixes(arr1)

        ans = 0
        for num in arr2:
            s = str(num)
            for i in range(len(s)):
                if s[: i + 1] in st:
                    ans = max(ans, i + 1)

        return ans
