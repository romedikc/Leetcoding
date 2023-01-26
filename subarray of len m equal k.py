def solution(a, m, k):
    count = 0
    sub_sum = 0
    hashTable = {}
    for i in range(len(a) - m + 1):
        sublist = a[i:i + m]
        for s in sublist:
            sub_sum += s
            if sub_sum == k:
                count += 1
            if sub_sum - k in hashTable:
                count += hashTable[sub_sum - k]
            if sub_sum in hashTable:
                hashTable[sub_sum] += 1
            else:
                hashTable[sub_sum] = 1

    return count


a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
m = 4
k = 10
print(solution(a, m, k))
