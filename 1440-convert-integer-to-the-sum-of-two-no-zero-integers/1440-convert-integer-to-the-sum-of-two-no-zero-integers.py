class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def valid(a, b):
            while a:
                if a % 10 == 0:
                    return False
                a //= 10
            while b:
                if b % 10 == 0:
                    return False
                b //= 10
            return True

        for a in range(1, n):
            b = n - a
            if valid(a, b):
                return [a, b]
        
        return []
