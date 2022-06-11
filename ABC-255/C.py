x, a, d, n = map(int, input().split())


if d < 0:
    final = a + (n - 1) * d
    a = final
    d *= -1

left = 0
right = n - 1

while right >= left:
    mid = (right + left) // 2
    if a + mid * d < x:
        left = mid + 1
    else:
        right = mid - 1

ans = 1 << 30
for i in range(max(0, left - 2), min(n + 1, right + 2)):
    ans = min(ans, abs(a + (i - 1) * d - x))

print(ans)
