n, w = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = set()
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            a = A[i] + A[j] + A[k]
            if a <= w:
                ans.add(a)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a = A[i] + A[j]
        if a <= w:
            ans.add(a)
for i in range(n):
    a = A[i]
    if a <= w:
        ans.add(a)

print(len(ans))
