sx, sy, gx, gy = map(int, input().split())

gy = -1 * gy

diff_x = abs(sx - gx)
diff_y = abs(sy-gy)

ans = 0

if sx <= gx:
    ans = sx + diff_x*abs(sy)/diff_y
else:
    ans = gx + diff_x*abs(gy)/diff_y
print(ans)
