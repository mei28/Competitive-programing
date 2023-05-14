MOD = 998244353


def solve(N):
    count = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            count[j] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += count[i] * count[i] * count[i]
        ans %= MOD
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
