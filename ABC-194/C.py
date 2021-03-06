from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
ans = 0

for i in range(-200, 201):
    for j in range(-200, 201):
        ans += (i - j) ** 2 * cnt[i] * cnt[j]
ans //= 2
print(ans)
