# スタックオーバーフローを防ぐ
import sys

sys.setrecursionlimit(10**6)

# 再帰関数 (A の前から i 個の中からいくつか選んで j を作れるか)


def func(i, j):
    # 過去に計算済みの場合メモに記録された値を返す
    if memo[i][j] != -1:
        return memo[i][j]

    # i = 0 のとき、 j = 0 なら true
    # それ以外のとき、問題文の通りに判定する
    if i == 0:
        memo[i][j] = j == 0
    else:
        memo[i][j] = 0
        if j >= A[i - 1] and func(i - 1, j - A[i - 1]) == 1:
            memo[i][j] = 1
        if func(i - 1, j) == 1:
            memo[i][j] = 1

    return memo[i][j]


# 入力
N, X = map(int, input().split())
A = list(map(int, input().split()))

# func(i, j) の値を記録するメモ(配列)を用意する
# -1 なら未記録、0 なら false、1 なら true

memo = [[-1] * (X + 1) for _ in range(N + 1)]

# 出力
if func(N, X) == 1:
    ans = "Yes"
else:
    ans = "No"
print(ans)
