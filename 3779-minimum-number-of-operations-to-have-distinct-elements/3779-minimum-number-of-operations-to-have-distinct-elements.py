class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dq = deque(nums)
        mp = Counter(nums)
        st = set()
        for key, val in mp.items():
            if val > 1:
                st.add(key)

        ans = 0
        while st:
            i = 0
            while dq and i < 3:
                val = dq.popleft()
                mp[val] -= 1
                if mp[val] <= 1 and val in st:
                    st.remove(val)
                    
                i += 1
            ans += 1
            
        return ans