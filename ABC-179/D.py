n, k = map(int, input().split())

S = set()
LR = []
for _ in range(k):
    tmp = list(map(int, input().split()))
    LR.append(tmp)

for i in LR:
    l, r = int(i[0]), int(i[1])
    for j in range(l, r + 1):
        S.add(j)

diff = n-1

ans = 0

MOD = 998244353

def dfs(A):
    if sum(A) == diff:
        return 1
    if sum(A) > diff:
        return 0
    res = 0
    for v in list(S):
        A.append(v)
        res = max(dfs(A)+res, dfs(A))
        res %= MOD
        A.pop()
    return res


print(dfs([]))
