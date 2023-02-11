n, m = map(int, input().split())
A = list(map(int, input().split()))

group = [[] for _ in range(n - m)]


j = 0
for i in range(1, n + 1):
    group[j].append(i)
    if i not in A:
        j += 1
ans = []

for g in group:
    ans += g[::-1]

print(*ans)
