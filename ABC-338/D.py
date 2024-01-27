def m(N, M, X):
    total_distance = sum(
        min(abs(X[i] - X[i - 1]), N - abs(X[i] - X[i - 1])) for i in range(1, M)
    )

    min_tour_length = total_distance

    for i in range(M - 1):
        if X[i] != X[i + 1]:
            distance_without_bridge = N - abs(X[i] - X[i + 1])
            additional_distance = distance_without_bridge - min(
                abs(X[i] - X[i + 1]), N - abs(X[i] - X[i + 1])
            )

            min_tour_length = min(min_tour_length, total_distance + additional_distance)

    return min_tour_length


N, M = map(int, input().split())
X = list(map(int, input().split()))

ans = m(N, M, X)
print(ans)
