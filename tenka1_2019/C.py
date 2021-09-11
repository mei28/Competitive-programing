from typing import List

n = int(input())
s = input()

# 累積和を取る
white_sum: List[int] = [0] * (n + 1)
black_sum: List[int] = [0] * (n + 1)


for i, j in enumerate(s):
    white_sum[i + 1] = white_sum[i] + int(j == ".")
    black_sum[i + 1] = black_sum[i] + int(j == "#")

res: int = 1 << 60

for l in range(n + 1):
    change_black = black_sum[l] - black_sum[0]
    change_white = white_sum[n] - white_sum[l]
    _res = change_black + change_white
    res = min(res, _res)

print(res)
