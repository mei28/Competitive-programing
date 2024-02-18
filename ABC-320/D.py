from collections import deque, defaultdict

N, M = map(int, input().split())

# グラフを初期化
graph = defaultdict(list)

for _ in range(M):
    A, B, X, Y = map(int, input().split())
    # 向きを元のノードからターゲットノードへの距離として記録
    graph[A].append((B, X, Y))
    # 逆方向の情報も追加
    graph[B].append((A, -X, -Y))

# BFSで各ノードの座標を計算
coords = dict()
coords[1] = (0, 0)
visited = set()
queue = deque([1])

while queue:
    current = queue.popleft()
    visited.add(current)
    x, y = coords[current]
    for next_node, dx, dy in graph[current]:
        if next_node in coords:
            # 既に座標が計算されている場合、矛盾していないかチェック
            if (x + dx, y + dy) != coords[next_node]:
                # print("undecidable")
                # exit()
                pass
        else:
            coords[next_node] = (x + dx, y + dy)
            if next_node not in visited:
                queue.append(next_node)

# 出力
for i in range(1, N + 1):
    if i in coords:
        print(*coords[i])
    else:
        print("undecidable")
