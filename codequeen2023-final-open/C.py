from collections import deque


def bfs(start, edges, N):
    visited = [False] * (N + 1)
    path = [[] for _ in range(N + 1)]  # Store the path for each vertex
    queue = deque([(start, [])])

    while queue:
        node, current_path = queue.popleft()
        path[node] = current_path + [node]
        for neighbor in edges[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path[node]))

    return path


def solve(N, S, T, edges):
    path_from_S = bfs(S, edges, N)
    path_from_T = bfs(T, edges, N)

    for j in range(1, N + 1):
        # Find the common vertices between the paths
        common_vertices = set(path_from_S[j]) & set(path_from_T[j])
        if j == S or j == T:
            print(len(common_vertices) - 1)
        else:
            print(len(common_vertices))


# Input reading
N, S, T = map(int, input().strip().split())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().strip().split())
    edges[u].append(v)
    edges[v].append(u)  # Since the graph is undirected

solve(N, S, T, edges)
