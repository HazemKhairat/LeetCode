class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        newArr = []
        for num in arr:
            tuble = (num, bin(num).count("1"))
            newArr.append(tuble)

        newArr = sorted(newArr, key=lambda x: (x[1], x[0]))
        ans = [x[0] for x in newArr]

        return ans
