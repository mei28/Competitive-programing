n = int(input())
S = input()
W = list(map(int, input().split()))

A = []
ans = 0
for s, w in zip(list(S), W):
    A.append([w, s])
    if s == "1":
        ans += 1

A = list(sorted(A, key=lambda x: x[0]))

x = ans
for i in range(n):
    if A[i][1] == "1":
        x -= 1
    else:
        x += 1

    if i < n - 1:
        if A[i][0] != A[i + 1][0]:
            ans = max(ans, x)
    else:
        ans = max(ans, x)

print(ans)
