from bisect import bisect_left


n = int(input())
A = list(map(int, input().split()))
S = sorted(list(set(A)))
ans = []
for a in A:
    idx = bisect_left(S, a)
    ans.append(idx + 1)
print(*ans)
