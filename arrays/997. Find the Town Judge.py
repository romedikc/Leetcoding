def findJudge(n: int, trust: List[List[int]]) -> int:
    count_yes = [0] * (n + 1)
    count_no = [0] * (n + 1)

    for i in range(len(trust)):
        count_yes[trust[i][1]] += 1
        count_no[trust[i][0]] += 1

    for i in range(1, n + 1):
        if count_yes[i] == n - 1 and count_no[i] == 0:
            return i

    return -1
