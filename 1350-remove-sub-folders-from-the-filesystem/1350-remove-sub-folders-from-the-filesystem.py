class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        st = set()
        for sub in folder:
            tmp = ""
            ok = True
            for ch in sub:
                tmp += ch
                if ch == '/' and tmp[:-1] in st:
                    ok = False
                    break
            if ok:
                st.add(sub)

        res = list(st)
        return res