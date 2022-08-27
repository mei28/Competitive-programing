import math

n = int(input())
A = list(map(int, input().split()))
S = [0]
# 適当な初期値を設定してやる。
# seq = 連続中の単調増加列の要素数
# prev = 前回の数
prev = 0
seq = 0
result = 0

for a in A:
    # 単調増加が続いていれば、要素数に 1 足す
    if a > prev:
        seq += 1
        prev = a
    else:
        # 単調増加が途切れたところで、組み合わせ数を足して
        # 次の単調増加列をスタートさせる
        result += (seq + 1) * seq // 2
        prev = a
        seq = 1

# 最後に残っている分を足してやること
result += (seq + 1) * seq // 2

print(result)
