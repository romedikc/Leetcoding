def minimumCost(cost: List[int]) -> int:
    cost.sort(reverse=True)
    remove_every_third_num = [cost[i] for i in range(len(cost)) if (i + 1) % 3 != 0]
    return sum(remove_every_third_num)


cost = [1, 2, 3]
print(minimumCost(cost))
