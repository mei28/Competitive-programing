# 入力
X = int(input())
A = list(map(int, input().split()))

# コインの金額
coins = [50, 10, 5, 1]

# 貪欲法
res = 0
for i in range(4):
    # コインの枚数制限 (A[i] 枚) がないときの枚数
    add = X // coins[i]

    # 枚数制限を考慮してコインの使用枚数を求める
    add = min(add, A[i])
    res += add
    # 残り金額を求める
    X -= coins[i] * add

# 出力
print(res)
