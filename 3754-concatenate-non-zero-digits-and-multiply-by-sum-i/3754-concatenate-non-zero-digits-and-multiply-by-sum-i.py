class Solution:
    def sumAndMultiply(self, n: int) -> int:
        st = ""
        sum = 0
        
        while n:
            st = str(n % 10) + st if (n % 10) != 0 else st
            sum += n % 10
            n //= 10

        return int(st) * sum if st else 0