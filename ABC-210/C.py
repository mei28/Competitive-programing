n, k = map(int, input().split())
C = list(map(int, input().split()))

ans = 1

s = C[0:k]
x = set(s)
ans = max(ans, len(x))
pre = C[0]
for i in range(k, n):
    now = C[i]
    pre = C[i - k]
    if now == pre:
        continue
    if now not in x:
        x.add(now)
        ans += 1
    # x.remove(pre)
    # x.add(C[i])
    # ans = max(ans, len(x))
    # pre = C[i - k + 1]
    # print(x)


print(ans)
