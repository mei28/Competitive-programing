import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
G = [[] for i in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

visited = [False] * n


ans = []


def dfs(now, last=-1):
    ans.append(now + 1)
    G[now].sort()
    for to in G[now]:
        if to == last:
            continue
        dfs(to, now)
        ans.append(now + 1)


dfs(0)
print(*ans)
