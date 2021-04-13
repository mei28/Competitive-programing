N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()


def solve(b):
    left = 0
    right = N - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        diff_left = b - A[left]
        diff_right = A[right] - b
        if diff_right > diff_left:
            right = mid
        else:
            left = mid
        pass

    diff_left = b - A[left]
    diff_right = A[right] - b
    if diff_right > diff_left:
        return left
    else:
        return right


ans = 0
for b in B:
    idx = solve(b)
    print(abs(b - A[idx]))
