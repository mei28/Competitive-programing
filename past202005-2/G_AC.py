from collections import deque, defaultdict

# グリッドの外壁の座標と、移動方向
OUTER_WALL = 202
MOVE_DIRECTIONS = ((1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1))


def construct_maze():
    # 障害物の座標を受け取って設置、外壁とゴールを設置する関数

    # 障害物を設置します
    for _ in range(n):
        ox, oy = map(int, input().split())
        grid[(ox, oy)] = "#"

    # 処理を楽にするために、外壁を作ります（番兵的なやつ）
    for i in range(-OUTER_WALL, OUTER_WALL + 1):
        grid[(OUTER_WALL, i)] = "#"
        grid[(-OUTER_WALL, i)] = "#"
        grid[(i, OUTER_WALL)] = "#"
        grid[(i, -OUTER_WALL)] = "#"

    # ゴールを設置します
    grid[(gx, gy)] = "G"


def bfs():
    que = deque()
    cx, cy, move_count = 0, 0, 0  # (現x座標, 現y座標, 移動回数)
    que.append((cx, cy, move_count))
    grid[(0, 0)] = "!"

    while que:
        cx, cy, move_count = que.popleft()

        for mx, my in MOVE_DIRECTIONS:
            nx = cx + mx
            ny = cy + my

            if grid[(nx, ny)] == ".":
                # 障害物がなく、まだ探索していないので、queに入れます
                que.append((nx, ny, move_count + 1))
                grid[(nx, ny)] = "!"  # 探索済みの印を付けます
            elif grid[(nx, ny)] == "G":
                # ゴールが見つかったので、現在の移動回数+1を返します
                return move_count + 1

    # ゴールできなかったので、-1を返します
    return -1


n, gx, gy = map(int, input().split())
grid = defaultdict(lambda: ".")  # construct_maze関数内で宣言すると、bfs関数内で使えません
construct_maze()
print(bfs())
