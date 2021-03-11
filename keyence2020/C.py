N, K, S = map(int, input().split())
ans = []
if S < 1e9:
    ans = [S for _ in range(K)] + [S + 1 for _ in range(N - K)]
else:
    ans = [S for _ in range(K)] + [1 for _ in range(N - K)]

print(*ans)
