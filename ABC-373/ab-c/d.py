from collections import defaultdict, deque


def solve_graph_constraints(n, edges):
    # Create adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, -w))

    # Initialize distances with None (unvisited)
    values = [None] * (n + 1)
    values[1] = 0  # Start from node 1 with value 0

    # Use a queue for BFS
    queue = deque([1])

    while queue:
        node = queue.popleft()
        current_value = values[node]

        for neighbor, weight in graph[node]:
            if values[neighbor] is None:
                # Set the value of the neighbor
                values[neighbor] = current_value + weight
                queue.append(neighbor)
            elif values[neighbor] != current_value + weight:
                # If a contradiction is found, there's an issue (this shouldn't happen in this problem)
                raise ValueError("Inconsistent solution detected")

    # Return the values excluding the 0th index (since nodes are 1-indexed)
    return values[1:]


# Input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Solve
result = solve_graph_constraints(n, edges)

# Output the result
for value in result:
    print(value)
