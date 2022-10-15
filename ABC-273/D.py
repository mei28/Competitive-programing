h, w, rs, cs = map(int, input().split())
rs -= 1
cs -= 1
n = int(input())
F = [[0] * w for _ in range(h)]
for _ in range(n):
    r, c = map(lambda x: int(x) - 1, input().split())
    F[r][c] = 1

q = int(input())
Qs = [input().split() for _ in range(q)]
dir = {"U": [-1, 0], "L": [0, -1], "D": [1, 0], "R": [0, 1]}


for l in Qs:
    d, a = l
    a = int(a)
    di = dir[d]
    dx = di[0]
    dy = di[1]
    for i in range(a):
        if 0 <= rs + dx < h and 0 <= cs + dy < w:
            try:
                if F[rs + dx][cs + dy] == 0:
                    rs += dx
                    cs += dy
                else:
                    break
            except:
                break
        else:
            break
    print(rs + 1, cs + 1)
