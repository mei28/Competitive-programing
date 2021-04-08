N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

left = -1
right = L + 1


def solve(M):
    pre = 0
    cnt = 0

    for i in range(0, N):
        if A[i] - pre >= M and L - A[i] >= M:
            cnt += 1
            pre = A[i]
    if cnt >= K:
        return True
    return False


left = -1
right = L + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if solve(mid):
        left = mid
    else:
        right = mid

print(left)
