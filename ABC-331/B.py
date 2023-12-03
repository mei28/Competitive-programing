from itertools import product

n, s, m, l = map(int, input().split())


def min_cost(N, S, M, L):
    max_packs_6 = (N + 5) // 6
    max_packs_8 = (N + 7) // 8
    max_packs_12 = (N + 11) // 12

    combinations = product(
        range(max_packs_6 + 1), range(max_packs_8 + 1), range(max_packs_12 + 1)
    )

    # Initialize minimum cost to a high value
    min_cost = float("inf")

    for combo in combinations:
        # Calculate the total number of eggs and total cost for the combination
        total_eggs = combo[0] * 6 + combo[1] * 8 + combo[2] * 12
        total_cost = combo[0] * S + combo[1] * M + combo[2] * L

        # Update minimum cost if this combination meets or exceeds the required number of eggs and is cheaper
        if total_eggs >= N and total_cost < min_cost:
            min_cost = total_cost

    return min_cost


ans = min_cost(n, s, m, l)
print(ans)
