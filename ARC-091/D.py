N, K = map(int, input().split())

if K == 0:
    print(N * N)
else:
    ans = 0
    for b in range(K + 1, N + 1):
        n = (N + 1) // b
        ans += n * (b - K) + max(0, N - (n * b + K) + 1)
    print(ans)
