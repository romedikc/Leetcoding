def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    mapping = {}
    for i in range(len(items1)):
        mapping[items1[i][0]] = items1[i][1]

    for j in range(len(items2)):
        if items2[j][0] in mapping:
            mapping[items2[j][0]] += items2[j][1]
        else:
            mapping[items2[j][0]] = items2[j][1]

    return sorted(mapping.items())


items1 = [[1, 3], [2, 2]]
items2 = [[7, 1], [2, 2], [1, 4]]
print(mergeSimilarItems(items1, items2))
