from collections import Counter

N = int(input())
A = list(map(lambda x: int(x) % 46, input().split()))
B = list(map(lambda x: int(x) % 46, input().split()))
C = list(map(lambda x: int(x) % 46, input().split()))

A.sort()
B.sort()
C.sort()

cnt_A = Counter(A)
cnt_B = Counter(B)
cnt_C = Counter(C)

A = set(A)
B = set(B)
C = set(C)

dp = [0] * 46

cnt = 0
for a in A:
    for b in B:
        for c in C:
            if (a + b + c) % 46 == 0:
                cnt += cnt_A[a] * cnt_B[b] * cnt_C[c]

print(cnt)
