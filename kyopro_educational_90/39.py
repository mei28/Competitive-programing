import sys

sys.setrecursionlimit(9000)


def dfs(v: int, p: int):
    dp[v] = 1
    for i in G[v]:
        if i == p:
            continue
        dfs(i, v)
        dp[v] += dp[i]


if __name__ == "__main__":
    N = int(input())
    A, B = [], []
    G = [[] for _ in range(1 << 20)]
    dp = [0] * (1 << 10)

    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A.append(a)
        B.append(b)
        G[a].append(b)
        G[b].append(a)

    dfs(0, -1)
    ans = 0
    for i in range(N - 1):
        r = min(dp[A[i]], dp[B[i]])
        ans += r * (N - r)

    print(ans)
