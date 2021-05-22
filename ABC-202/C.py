from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))
cnt_C = Counter(C)
cnt_A = Counter(A)
cnt_B = Counter(B)
dct_B = dict()

for i, b in enumerate(B):
    dct_B.setdefault(b, []).append(i)

set_A = set(A)
set_C = set(C)

tmp_B = set()
for k, v in cnt_C.items():
    tmp_B.add(B[k])

ans = 0
for a in set_A:
    if a in tmp_B:
        idx = dct_B[a]
        for i in idx:
            ans += cnt_A[a] * cnt_C[i]

print(ans)
