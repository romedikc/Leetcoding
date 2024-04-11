def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    deck.sort()
    q = deque()
    for c in deck[::-1]:
        if q:
            q.appendleft(q.pop())
        q.appendleft(c)
    return q


deck = [17, 13, 11, 2, 3, 5, 7]
print(deckRevealedIncreasing(deck))
