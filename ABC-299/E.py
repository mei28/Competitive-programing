from collections import defaultdict, deque


def bfs(graph, start):
    visited = set()
    distances = defaultdict(int)
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


def solve(N, M, edges, K, conditions):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distances = bfs(graph, 1)
    black_nodes = set()

    for p, d in conditions:
        if distances[p] == d:
            black_nodes.add(p)

    if len(black_nodes) == 0:
        return "No"
    else:
        return "Yes", black_nodes


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
conditions = [list(map(int, input().split())) for _ in range(K)]
result = solve(N, M, edges, K, conditions)
print(result)  # 出力: ('Yes', {3})
