def count_strings(S):
    N = len(S)
    mod = 998244353

    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Iterate through the string S
    for i in range(N):
        for j in range(i + 1):
            # If S[i] is the j-th character of an arbitrary string
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= mod

            # If S[i] is not the j-th character of an arbitrary string
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod

    # Calculate the result
    result = (2 * sum(dp[N]) - dp[N][0]) % mod
    return result


# Input
S = input()

# Solve the problem
print(count_strings(S))
