class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        i = j = 0
        players.sort()
        trainers.sort()

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
                res += 1

            j += 1                

        return res