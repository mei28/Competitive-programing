from collections import Counter

n = int(input())
A = list(map(int, input().split()))

cnter = Counter(A)

ans = 0
keys = cnter.keys()
for i in keys:
    for j in keys:
        if i == j:
            continue
        ans += ((i - j) ** 2) * cnter[i] * cnter[j]
print(ans // 2)
