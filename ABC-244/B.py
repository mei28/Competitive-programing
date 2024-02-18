n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

idx = 0

x, y = 0, 0

T = list(input())

for t in T:
    if t == "S":
        x += dx[idx]
        y += dy[idx]
    else:
        idx += 1
        idx %= 4

print(x, y)
