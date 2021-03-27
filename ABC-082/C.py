from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)

cnt = 0
for k, v in c.items():
    if k == v:
        continue
    elif k < v:
        cnt += v - k
    else:
        cnt += v

print(cnt)
