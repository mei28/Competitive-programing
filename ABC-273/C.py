from collections import Counter

n = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = Counter(A)


keys = list(cnt.keys())
keys.sort()
C = {i: v for i, v in enumerate(keys[::-1])}

ans = {i: 0 for i in range(n)}
for k, v in C.items():
    ans[k] = cnt[v]
for _, v in ans.items():
    print(v)
