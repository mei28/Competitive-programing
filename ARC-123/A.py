a, b, c = map(int, input().split())

ans = 0
x, y = c - b, b - a

if x > y:
    ans += (x - y) // 2
    x = y + (x - y) % 2
    if x > y:
        ans += 1
        x -= 2

ans += y - x
print(ans)
