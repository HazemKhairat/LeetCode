class Solution:
    def intersectionSizeTwo(self, l: List[List[int]]) -> int:
        l = sorted(l, key=lambda x: x[1])
        st = SortedSet()
        st.add(l[0][1])
        st.add(l[0][1] - 1)

        for i in range(1, len(l)):
            cnt = 0
            for num in st:
                if num >= l[i][0] and num <= l[i][1]:
                    cnt += 1

            if cnt == 0:
                st.add(l[i][1])
                st.add(l[i][1] - 1)
            elif cnt == 1:
                if l[i][1] not in st:
                    st.add(l[i][1])
                else:
                    st.add(l[i][1] - 1)
            else:
                continue

        return len(st)
