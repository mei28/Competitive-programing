n = int(input())
A = list(map(int, input().split()))
d = int(input())
S = [[] for _ in range(n + 2)]
T = set(A)

for i in range(n):
    S[i + 1] = S[i] + [A[i]]
for _ in range(d):
    l, r = map(lambda x: int(x) - 1, input().split())
    left = S[l]
    right = S[n][r + 1 :]
    ans = max(left + right)
    # print(left, right)
    print(ans)
