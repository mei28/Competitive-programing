n, p, q = map(int, input().split())
D = list(map(int, input().split()))

ans = p

for d in D:
    ans = min(ans, d + q)
print(ans)
