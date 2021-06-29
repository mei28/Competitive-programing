from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
B, C = [], []
for _ in range(m):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

cnter = Counter(A)

for b, c in zip(B, C):
    cnter[c] += b

cnter = dict(sorted(cnter.items(), key=lambda x: x[0], reverse=True))

ans = 0
for k, v in cnter.items():
    if n == 0:
        break
    if n >= v:
        ans += k * v
        n -= v
    else:
        ans += k * n
        break

print(ans)
