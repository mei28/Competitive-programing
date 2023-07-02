from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 上下左右への移動
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 各ステップで進むべき文字
snuke = "snuke"

# 訪れたことがあるかどうかを記録する配列
visited = [[[False] * 5 for _ in range(W)] for _ in range(H)]

# BFSのためのキュー
q = deque([(0, 0, 0)])

# スタート位置を訪れたことにする
visited[0][0][0] = True

while q:
    x, y, t = q.popleft()

    # 辺で隣接するマスを調べる
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nt = (t + 1) % 5

        # マスが範囲外ならスキップ
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue

        # 訪れたことがあるならスキップ
        if visited[nx][ny][nt]:
            continue

        # 移動先のマスの文字が次に進むべき文字かを確認
        if S[nx][ny] == snuke[nt]:
            q.append((nx, ny, nt))
            visited[nx][ny][nt] = True

# ゴール位置に訪れたことがあるかをチェック
if any(visited[H - 1][W - 1]):
    print("Yes")
else:
    print("No")
