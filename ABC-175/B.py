import itertools

N = int(input())
L = map(int, input().split())

C = list(itertools.combinations(L, 3))

cnt = 0
for a, b, c in C:
    if a == b or b == c or a == c:
        continue

    maxhen = max(max(a, b), c)
    if maxhen < (a + b + c - maxhen):
        cnt += 1

print(cnt)
