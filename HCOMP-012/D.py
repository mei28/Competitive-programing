n = int(input())

XYH = [list(map(int, input().split())) for _ in range(n)]

xx = yy = _h = -1
for x, y, h in XYH:
    if h != 0:
        xx = x
        yy = y
        _h = h
        break

for i in range(0, 101):
    for j in range(0, 101):
        hhh = _h + abs(i - xx) + abs(j - yy)
        flg = True
        for x, y, h in XYH:
            hh = max(hhh - abs(x - i) - abs(y - j), 0)
            if h != hh:
                flg = False
        if flg:
            print(i, j, hhh)
            exit()
