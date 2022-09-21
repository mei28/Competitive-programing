n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    left = -1
    right = n - 1
    while right - left > 1:
        mid = (right + left) // 2
        if b <= A[mid]:
            right = mid
        else:
            left = mid
    print(right)
