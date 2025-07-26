class Solution:
    def partitionString(self, s: str) -> List[str]:
        st = set()
        res = []
        tmp = ""
        for ch in s:
            tmp += ch
            if tmp not in st:
                st.add(tmp)
                res.append(tmp)
                tmp = ""
        
        return res