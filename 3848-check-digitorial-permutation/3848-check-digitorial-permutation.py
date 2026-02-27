class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        fact = [1] * 10
        for i in range(1, 10):
            fact[i] = i * fact[i -1]
        
        arr1 = []
        cnt1 = [0] * 10
        tmp = n
        res = 0

        while tmp:
            arr1.append(tmp % 10)
            cnt1[tmp%10] += 1
            res += fact[tmp % 10]
            tmp //= 10

        arr2 = []
        cnt2 = [0] * 10

        while res:
            arr2.append(res % 10)
            cnt2[res%10] += 1
            res //= 10
        # print(arr1)
        # print(arr2)
        # print(cnt1)
        # print(cnt2)
        if len(arr1) != len(arr2): return False
        for i in range(len(cnt1)):
            if cnt1[i] != cnt2[i]:
                return False
        return True