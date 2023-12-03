def solve(N, M, L, main_dishes, side_dishes, bad_combinations):
    sorted_side_dishes = sorted(
        [(price, i) for i, price in enumerate(side_dishes, start=1)], reverse=True
    )

    bad_combinations_set = set((c, d) for c, d in bad_combinations)

    max_prices = -1
    for i, main_price in enumerate(main_dishes, start=1):
        for side_price, side_index in sorted_side_dishes:
            if (i, side_index) not in bad_combinations_set:
                max_prices = max(max_prices, main_price + side_price)
                break

    return max_prices


N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = set(tuple(map(int, input().split())) for _ in range(L))
print(solve(N, M, L, A, B, CD))
