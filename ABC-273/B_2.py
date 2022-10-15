x, k = map(int, input().split())

ans = x

for i in range(k + 1):
    ans = round(ans + 0.1, -(i))
    ans = int(ans)
print(ans)
