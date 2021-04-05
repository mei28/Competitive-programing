x, y = map(int, input().split())
ans = 10e9

if x <= y:
    ans = min(ans, y - x)
if -x <= y:
    ans = min(ans, y + x + 1)
if x <= -y:
    ans = min(ans, -y - x + 1)
if -x <= -y:
    ans = min(ans, -y + x + 2)

print(ans)
