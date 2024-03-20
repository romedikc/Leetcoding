def leastInterval(tasks: List[str], n: int) -> int:
    freq = Counter(tasks)
    max_freq = max(freq.values())
    num_max_freq_tasks = sum(1 for task, f in freq.items() if f == max_freq)

    return max(len(tasks), (max_freq - 1) * (n + 1) + num_max_freq_tasks)


# (max_freq - 1) * (n + 1) calculates the number of intervals required
# for tasks other than the ones with maximum frequency, while considering the cooling time constraint.
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))
