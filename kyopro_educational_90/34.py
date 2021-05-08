N, K = map(int, input().split())
A = list(map(int, input().split()))
dct = {}

for a in A:
    dct[a] = 0

cr = 0
cnt = 0
ans = 0
for i in range(N):
    while cr < N:
        if dct[A[cr]] == 0 and cnt == K:
            break
        if dct[A[cr]] == 0:
            cnt += 1
        dct[A[cr]] += 1
        cr += 1
    ans = max(ans, cr - i)
    if dct[A[i]] == 1:
        cnt -= 1
    dct[A[i]] -= 1

print(ans)
