def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # adjacency list
    prereq = {c: [] for c in range(numCourses)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    output = []
    visited, cycle = set(), set()

    def dfs(crs):
        # detected cycle
        if crs in cycle:
            return False
            # don't need to visit twice
        if crs in visited:
            return True
        cycle.add(crs)
        for pre in prereq[crs]:
            # detected cycle
            if dfs(pre) == False:
                return False
        cycle.remove(crs)
        visited.add(crs)
        output.append(crs)
        return True

    for c in range(numCourses):
        if dfs(c) == False:
            return []
    return output


numCourses = 2
prerequisites = [[1, 0]]
print(findOrder(numCourses, prerequisites))
