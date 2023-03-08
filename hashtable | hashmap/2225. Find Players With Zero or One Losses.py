from collections import Counter


# crazy brute force, might rewrite later

def findWinners(matches):
    winners = {}
    losers = {}
    a, b = [], []
    for i in matches:
        if i[0] in winners:
            winners[i[0]] += 1
        else:
            winners[i[0]] = 1
        if i[1] in losers:
            losers[i[1]] += 1
        else:
            losers[i[1]] = 1

    for k in winners.keys():
        if k not in losers:
            a.append(k)
    for k, v in losers.items():
        if v == 1:
            b.append(k)

    a.sort()
    b.sort()
    return [a, b]


matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
print(findWinners(matches))
