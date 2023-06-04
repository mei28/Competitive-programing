class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

        return True


def is_good_graph(graph, n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if uf.union(u, v):
            graph[u].append(v)
            graph[v].append(u)
        else:
            return False
    return True


def check_good_graph(n, m, edge_list, k, path_list, q, query_list):
    graph = [[] for _ in range(n + 1)]
    edges = []
    for u, v in edge_list:
        edges.append((u, v))

    if not is_good_graph(graph, n, edges):
        return ["No"] * q

    results = []
    for p, q in query_list:
        graph_copy = [lst[:] for lst in graph]
        graph_copy[p].append(q)
        graph_copy[q].append(p)
        if is_good_graph(graph_copy, n, edges):
            results.append("Yes")
        else:
            results.append("No")
    return results


# 入力の読み込み
n, m = map(int, input().split())
edge_list = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path_list = [list(map(int, input().split())) for _ in range(k)]
q = int(input())
query_list = [list(map(int, input().split())) for _ in range(q)]

# 良いグラフかどうかを判定して質問に回答する
results = check_good_graph(n, m, edge_list, k, path_list, q, query_list)

# 結果を出力
for result in results:
    print(result)
