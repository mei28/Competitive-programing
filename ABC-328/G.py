def min_cost_to_equalize(A, B, C, N):
    # Initialize the DP array with infinite cost
    dp = [float("inf")] * (1 << N)
    dp[0] = 0  # Base case: no elements matched yet

    # Iterate over all the states of the DP
    for mask in range(1 << N):
        for i in range(N):
            # If the ith element of A is not matched yet
            if not (mask & (1 << i)):
                # Calculate the cost to add k to A[i] to match B[i]
                cost_to_match_i = abs(A[i] - B[i])
                # Update the DP state if this is a lower cost option
                dp[mask | (1 << i)] = min(
                    dp[mask | (1 << i)], dp[mask] + cost_to_match_i
                )

                for j in range(i + 1, N):
                    # If the jth element of A is not matched yet
                    if not (mask & (1 << j)):
                        # Calculate the cost for splitting at position i and j
                        cost_for_split = C
                        # Calculate the cost to match both A[i] and A[j] to B[i] and B[j]
                        cost_to_match_i_and_j = cost_to_match_i + abs(A[j] - B[j])
                        # Update the DP state if this is a lower cost option
                        dp[mask | (1 << i) | (1 << j)] = min(
                            dp[mask | (1 << i) | (1 << j)],
                            dp[mask] + cost_for_split + cost_to_match_i_and_j,
                        )

    # The final state where all elements are matched is 2^N - 1
    final_state = (1 << N) - 1
    return dp[final_state]


# Input format
n, c = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Call the function with the provided inputs
min_cost = min_cost_to_equalize(A, B, c, n)
print(min_cost)
