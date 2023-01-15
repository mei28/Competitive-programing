from collections import Counter


n = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
ans = 0
for v in cnt.values():
    if v >= 3:
        ans += v * (v - 1) * (v - 2) // 6
print(ans)
