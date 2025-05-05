class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        i = j = 0
        matches = 0
        while i < len(players) and j <len(trainers):
            if trainers[j] >= players[i]:
                matches +=1
                i += 1
            j+= 1
        return matches

        