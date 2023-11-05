import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)


def dfs(node, color):
    colors[node] = color
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
        if colors[neighbor] == -1:
            if not dfs(neighbor, 1 - color):
                return False
    return True


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

graph = defaultdict(list)
for i in range(M):
    graph[A[i]].append(B[i])
    graph[B[i]].append(A[i])

colors = [-1] * (N + 1)

is_bipartite = True
for i in range(1, N + 1):
    if colors[i] == -1:
        if not dfs(i, 0):
            is_bipartite = False
            break

print("Yes" if is_bipartite else "No")
