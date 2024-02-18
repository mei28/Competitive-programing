H, W = map(int, input().split())
A = []
for i in range(H):
    l = list(map(int, input().split()))
    for j in l:
        A.append(j)


_min = min(A)

ans = 0

for i in A:
    ans += i - _min

print(ans)
