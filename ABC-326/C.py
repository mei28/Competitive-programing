def max_presents(N, M, A):
    A.sort()

    l, r = 0, 0
    ans = 0
    while r < N:
        if A[r] - A[l] < M:
            ans = max(ans, r - l + 1)
            r += 1
        else:
            l += 1
    return ans


N, M = map(int, input().split())
A = list(map(int, input().split()))

print(max_presents(N, M, A))
