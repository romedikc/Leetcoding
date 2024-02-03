def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    starting_position = 0
    total = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            total = 0
            starting_position = i + 1
    return starting_position


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))
