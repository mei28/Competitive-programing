N, K = map(int, input().split())

A = list(map(int, input().split()))

A.sort()
max_A = max(A)
dct = {}


for i in range(max_A+1):
    dct[i] = K
for i in A:
    dct[i] -= 1


cnt = 0
ans = 0
for i, v in dct.items():
    if cnt < v:
        ans += (v-cnt)*i
        cnt = v

if cnt < K:
    ans += (max_A+1)*(K-cnt)

print(ans)
