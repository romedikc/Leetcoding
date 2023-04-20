def topKFrequent(words: List[str], k: int) -> List[str]:
    freq = Counter(words)
    heap = [(-freq[word], word) for word in freq]
    heapq.heapify(heap)
    output = []
    for i in range(k):
        freq, word = heapq.heappop(heap)
        output.append(word)
    return output


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(words, k))
