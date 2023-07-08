import heapq

INF = float("inf")


def dijkstra(graph, start):
    dist = [INF] * len(graph)
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        v = heapq.heappop(queue)[1]
        for w, cost in graph[v]:
            if dist[w] > dist[v] + cost:
                dist[w] = dist[v] + cost
                heapq.heappush(queue, (dist[w], w))
    return dist


def main():
    N_1, N_2, M = map(int, input().split())
    graph = [[] for _ in range(N_1 + N_2 + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dist = dijkstra(graph, 1)
    dist1 = -1
    for d in dist:
        if d != INF:
            dist1 = max(dist1, d)
    dist = dijkstra(graph, N_1 + N_2)
    dist2 = -1
    for d in dist:
        if d != INF:
            dist2 = max(dist2, d)
    print(dist1 + dist2 + 1)


if __name__ == "__main__":
    main()
