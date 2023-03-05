from collections import deque


def bfs(graph, visited, v):
    num_vertices, num_edges = 0, 0
    q = deque([v])
    visited[v] = True
    while q:
        u = q.popleft()
        num_vertices += 1
        for neighbor in graph[u]:
            num_edges += 1
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return num_vertices, num_edges // 2


def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n + 1)
    for v in range(1, n + 1):
        if not visited[v]:
            num_vertices, num_edges = bfs(graph, visited, v)
            if not num_vertices == num_edges:
                print("No")
                exit()
    print("Yes")


solve()
