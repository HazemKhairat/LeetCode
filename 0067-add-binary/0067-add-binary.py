class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def convertToDice(st):
            res = 0
            arr = list(st)
            arr = arr[::-1]
            for i in range(len(arr)):
                digit = int(arr[i])
                res += (2**i) * digit
            return res

        total = convertToDice(a) + convertToDice(b)

        def convertToBinary(num):
            res = ""
            while num:
                digit = num % 2
                num //= 2
                res += str(digit)
            return res[::-1]

        ans = convertToBinary(total) 
        return ans if ans else "0"
