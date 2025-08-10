class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        st = set()
        dg1 = ""
        while n:
            dg1 += str(n % 10)
            n //= 10
        s1 = ''.join(sorted(dg1))

        for i in range(31):
            st.add(2**i)
        
        for item in st:
            tmp = item
            dg2 = ""
            while tmp:
                dg2 += str(tmp % 10)
                tmp //= 10
            s2 = ''.join(sorted(dg2))
            if s1 == s2:
                return True
        return False


