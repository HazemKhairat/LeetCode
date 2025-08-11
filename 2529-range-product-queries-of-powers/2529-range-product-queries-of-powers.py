class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        st = SortedSet()
        MOD = 10**9 + 7
        num = 1
        for i in range(1, 32):
            st.add(num)
            num *= 2

        arr = []
        for i in range(31):
            if (n & 1):
                arr.append(st[i])
            n >>= 1
        # print(arr)
        
        for i in range(1, len(arr)):
            arr[i] *= arr[i - 1]
        pref = [1] + arr
        # print(pref)

        ans = []
        for q in queries:
            r = q[1] + 1
            l = q[0]
            ans.append((pref[r] // pref[l]) % MOD)
            

        return ans
