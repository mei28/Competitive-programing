n = int(input())
A = list(map(int, input().split()))

A.sort()
cnt = sum(map(lambda x: x < 0, A))


A = list(map(lambda x: abs(x), A))
A.sort()
if cnt % 2 == 0:
    print(sum(A))
else:
    ans = 0
    for i in range(n):
        if i == 0:
            ans = -abs(A[i])
        else:
            ans += abs(A[i])

    print(ans)
