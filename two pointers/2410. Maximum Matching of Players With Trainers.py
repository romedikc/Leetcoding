def matchPlayersAndTrainers(players, trainers):
    players.sort()
    trainers.sort()
    i, j = 0, 0
    count = 0
    while i < len(players) and j < len(trainers):
        if players[i] <= trainers[j]:
            count += 1
            i += 1
        j += 1
    return count


players = [4, 7, 9]
trainers = [8, 2, 5, 8]
print(matchPlayersAndTrainers(players, trainers))
