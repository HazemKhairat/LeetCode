class Solution:
    def findEvenNumbers(self, dig: List[int]) -> List[int]:
        n = len(dig)
        res = []
        seen = set()
        for x in range(n):
            for y in range(n):
                if y == x:
                    continue
                for z in range(n):
                    if z == x or z == y:
                        continue
                    string = str(dig[x]) + str(dig[y]) + str(dig[z])
                    if string[0] != "0" and int(string) % 2 == 0 and string not in seen:
                        seen.add(string)
                        res.append(int(string))

        res.sort()
        return res
