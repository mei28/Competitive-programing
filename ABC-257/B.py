n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

ans = [False] * (n + 1)
ans_idx = [-2] + [a for a in A]
for a in A:
    ans[a] = True

for l in L:
    a = ans_idx[l]
    if a >= n:
        continue
    elif a + 1 <= n and ans[a + 1] == False:
        ans[a + 1] = True
        ans[a] = False
        ans_idx[l] = a + 1


print(*ans_idx[1:])

