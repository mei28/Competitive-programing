N = int(input())
T = list(map(int, input().split()))

T.sort(reverse=True)
a, b = 0, 0

for t in T:
    if a < b:
        a += t
    else:
        b += t
tmp_a = max(a, b)

T.sort()
a, b = 0, 0

for t in T:
    if a < b:
        a += t
    else:
        b += t
tmp_b = max(a, b)

print(min(tmp_a, tmp_b))
