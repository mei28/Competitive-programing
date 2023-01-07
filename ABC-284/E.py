from queue import PriorityQueue

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

children = G


def count_simple_paths(node: int) -> int:
    # node の子ノードを起点とする単純パスの個数を数える
    count = 0
    for child in children[node]:
        count += count_simple_paths(child)
    # node を起点とする単純パスを 1 つ追加
    count += 1
    return min(count, 1000000)


print(count_simple_paths(0))
