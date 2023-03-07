from collections import Counter

n = int(input())
A = list(map(lambda x: int(x), input().split()))
cnt = Counter(A)

for i in range(1, n + 1):
    print(cnt.get(i) if cnt.get(i) else 0)
