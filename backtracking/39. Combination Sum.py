def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    output = []

    def dfs(i, cur, total):
        if total == target:
            output.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return
        # decision to add
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        # decision to not add
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return output


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
