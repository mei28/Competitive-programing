import math

n = int(input())

max_L = -float("inf")
min_R = float("inf")

for i in range(n):
    l, r = map(int, input().split())
    max_L = max(max_L, l)
    min_R = min(min_R, r)

    if max_L <= min_R:
        print(0)
    else:
        tmp = math.ceil(abs(max_L - min_R) / 2)
        print(tmp)
