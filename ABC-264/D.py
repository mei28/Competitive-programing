S = input()

T = "atcoder"

A = []
for s in S:
    # A.append([T.index(s), s])
    A.append(T.index(s))


ans = 0

for i in range(len(S)):
    for j in range(len(S) - i - 1):
        if A[j] > A[j + 1]:
            ans += 1
            A[j + 1], A[j] = A[j], A[j + 1]

print(ans)
