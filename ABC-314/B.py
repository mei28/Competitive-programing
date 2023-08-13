n = int(input())
Cs = []
As = []
for _ in range(n):
    c = int(input())
    Cs.append(c)
    A = list(map(int, input().split()))
    As.append(A)
x = int(input())

ans = []
min_len = 10**9
for i in range(n):
    a = As[i]
    if x in a:
        ans.append((i + 1, len(a)))
        min_len = min(min_len, len(a))
ans = sorted(ans, key=lambda x: x[1])

anss = []

for i, a in ans:
    if a != min_len:
        break
    anss.append(i)

if len(anss) == 0:
    print(0)
else:
    print(len(anss))
    print(*anss)
