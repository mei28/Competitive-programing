n, k = map(int, input().split())
A = list(map(int, input().split()))
add = k - n % k
A = A + [-1] * add
_min = min(A)
print(A)
