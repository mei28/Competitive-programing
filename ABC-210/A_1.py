n, a, x, y = map(int, input().split())

ans = a * x
if n - a > 0:
    ans += (n - a) * y

print(ans)
