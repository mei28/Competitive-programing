def max_dishes(N, Q, A, B):
    max_a_dishes = [q // a if a != 0 else float("inf") for q, a in zip(Q, A)]
    max_b_dishes = [q // b if b != 0 else float("inf") for q, b in zip(Q, B)]

    max_people = 0
    for a_dishes in range(min(max_a_dishes) + 1):
        remaining_q = [q - a * a_dishes for q, a in zip(Q, A)]

        b_dishes = min(
            [q // b if b != 0 else float("inf") for q, b in zip(remaining_q, B)]
        )

        max_people = max(max_people, a_dishes + b_dishes)

    return max_people


N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(max_dishes(N, Q, A, B))
