n = int(input())
A = list(map(int, input().split()))


ans = 0
itti = [0] * (n + 1)
for i in range(0, n):
    itti[i + 1] = itti[i]
    if i + 1 == A[i]:
        itti[i + 1] += 1


for i, a in enumerate(A):
    if a != i + 1:
        if A[a - 1] == i + 1 and i < a:
            ans += 1
    else:
        ans += itti[n] - itti[i + 1]

print(ans)
