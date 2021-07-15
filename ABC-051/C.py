sx, sy, tx, ty = map(int, input().split())

ans = ""

dx = abs(tx - sx)
dy = abs(ty - sy)

# first
ans += "R" * dx
ans += "U" * dy
ans += "L" * dx
ans += "D" * dy

# second
ans += "D"
ans += "R" * (dx + 1)
ans += "U" * (dy + 1)
ans += "L"
ans += "U"
ans += "L" * (dx + 1)
ans += "D" * (dy + 1)
ans += "R"
print(ans)
