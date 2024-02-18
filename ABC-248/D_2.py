from bisect import bisect_left, bisect_right

n = int(input())
A = list(map(int, input().split()))
q = int(input())
Qs = [list(map(int, input().split())) for _ in range(q)]


dct = [[] for _ in range(n + 1)]

for i, a in enumerate(A, 1):
    dct[a].append(i)

for l, r, x in Qs:
    B = dct[x]
    left_idx = bisect_left(B, l)
    right_idx = bisect_right(B, r)
    print(right_idx - left_idx)
