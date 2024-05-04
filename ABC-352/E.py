class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(edges, n):
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = 0

    for weight, u, v in sorted(edges):
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += weight
            mst_edges += 1
            if mst_edges == n - 1:
                break

    if mst_edges == n - 1:
        return mst_cost
    else:
        return None


n, m = map(int, input().split())
edges = []
from collections import defaultdict
import heapq

edges = []
edge_dict = defaultdict(list)
for a in range(m):
    k, c = map(int, input().split())
    vertices = list(map(int, input().split()))

    base_vertex = vertices[0] - 1
    for vertex in vertices[1:]:
        vertex -= 1
        edges.append((c, base_vertex, vertex))

mst_cost = kruskal(edges, n)
if mst_cost is not None:
    print(mst_cost)
else:
    print(-1)
