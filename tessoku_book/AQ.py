n, l = map(int, input().split())

ans = 0
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == "E":
        ans = max(l - a, ans)
    else:
        ans = max(a, ans)
print(ans)
