def minimumCardPickup(cards):
    indices = {}
    min_diff = -1
    for i in range(len(cards)):
        if cards[i] in indices:
            curr_diff = i - indices[cards[i]]
            if curr_diff < min_diff or min_diff == -1:
                min_diff = curr_diff + 1
        indices[cards[i]] = i
    return min_diff


cards = [3, 4, 2, 3, 4, 7]
print(minimumCardPickup(cards))
