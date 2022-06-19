from collections import deque

n = int(input())
A = [i for i in range(1, n + 1)]
X = list(map(int, input().split()))
C = list(map(int, input().split()))
G = [[] for _ in range(n)]
for i, x in enumerate(X):
    x -= 1
    G[x].append(i)

deg = [0] * n
for i in range(n):
    deg[i] = len(G[i])

tmp = []
print(G)
for i, g in enumerate(G):
    if g == []:
        tmp.append([i, C[i]])

tmp = list(sorted(tmp, key=lambda x: x[1]))
ans = [i[0] for i in tmp]
deq = deque(ans)
COST = [[i, C[i]] for i in range(n)]
COST = list(sorted(COST, key=lambda x: x[1]))
