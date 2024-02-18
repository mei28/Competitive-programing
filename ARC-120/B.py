h, w = map(int, input().split())
S = []
MOD = 998244353
for _ in range(h):
    s = input()
    S.append(s)

# 0:., 1:R, 2:B, 3:矛盾
color_by_dist = [0] * (h + w - 1)

for _h in range(h):
    for _w in range(w):
        dist = _h + _w
        if S[_h][_w] == "R":
            color = 1
        elif S[_h][_w] == "B":
            color = 2
        else:
            color = 0

        color_by_dist[dist] |= color

result = 1

for d in range(h + w - 1):
    if color_by_dist[d] == 3:
        print(0)
        exit()

    elif color_by_dist[d] == 0:
        result *= 2
        result %= MOD


print(result)
