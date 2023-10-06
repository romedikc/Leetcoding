# O(n^2)
def integerBreak(n: int) -> int:
    # store the maximum product for each integer from 1 to n.
    dp = {1: 1}
    # Loop through integers from 2 to n (inclusive).
    for num in range(2, n + 1):
        # Initialize dp[num] to 'num' (the product of a single integer), unless num is equal to 'n'.
        dp[num] = 0 if num == n else num
        # Iterate through integers from 1 to 'num'.
        for i in range(1, num):
            # Calculate the product of breaking 'num' into 'i' and 'num - i'.
            val = dp[i] * dp[num - i]
            # Update dp[num] with the maximum product between its current value and 'val'.
            dp[num] = max(dp[num], val)
    return dp[n]


n = 10
print(integerBreak(n))
