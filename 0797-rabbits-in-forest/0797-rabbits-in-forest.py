class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        map = Counter(answers)
        res = 0

        for color, counter in map.items():
            groupSize = color + 1
            numOfGroups = ceil(counter / groupSize)
            res += numOfGroups * groupSize

        return res
