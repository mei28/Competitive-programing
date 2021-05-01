import sys

sys.setrecursionlimit(10 ** 6)


def dfs(v: int, p: int = -1) -> None:
    if cnt[color[v]] == 0:
        ans.append(v + 1)
    cnt[color[v]] += 1
    for u in to[v]:
        if u == p:
            continue
        dfs(u, v)
    cnt[color[v]] -= 1


if __name__ == "__main__":
    N = int(input())
    color = [0] * N
    cnt = [0] * 100005
    to = [[] for _ in range(N)]
    ans = []

    color = list(map(int, input().split()))
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)
    dfs(0, -1)

    ans.sort()
    print(*ans)
