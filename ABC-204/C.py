import sys

sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
# G = [[0] * N for _ in range(N)]

G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)


ans = [set() for _ in range(N + 1)]


def dfs(v: int, p: int = -1, idx=0):
    ans[idx].add(v)
    if len(ans[idx]) >= N:
        return
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, idx)


for i in range(1, N + 1):
    dfs(i, -1, i)
cnt = 0
ans = ans[1:]

for a in ans:
    if len(a) == 0:
        cnt += 1
    else:
        cnt += len(a)


print(cnt)
