from itertools import combinations


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_v] += 1
        return True


def find_minimum_spanning_tree_cost(edges, n, k):
    min_cost_mod_k = float("inf")
    for combo in combinations(edges, n - 1):
        union_find = UnionFind(n)
        cost = 0
        for u, v, w in combo:
            if not union_find.union(u, v):
                break
            cost += w
        else:
            min_cost_mod_k = min(min_cost_mod_k, cost % k)
    return min_cost_mod_k


n, m, k = map(int, input().split())

edges = []
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v, w))
print(find_minimum_spanning_tree_cost(edges, n, k))
