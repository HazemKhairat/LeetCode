class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
        li1 = v1.split('.')
        li2 = v2.split('.')

        while len(li1) < len(li2): li1.append('0')
        while len(li2) < len(li1): li2.append('0')

        for i in range(len(li1)):
            if int(li1[i]) < int(li2[i]): return -1
            elif int(li1[i]) > int(li2[i]): return 1

        return 0