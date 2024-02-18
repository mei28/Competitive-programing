from bisect import bisect_left, bisect_right

n = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()
C = list(map(int, input().split()))
C.sort()

ans = 0


for b in B:
    a_ = bisect_left(A, b)
    c_ = len(C) - bisect_right(C, b)

    ans += a_ * c_

print(ans)
