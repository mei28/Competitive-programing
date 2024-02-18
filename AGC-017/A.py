N, P = map(int, input().split())
A = list(map(int, input().split()))

even = 0
odd = 0

for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

even_cnt = 2**even
if odd == 0:
    if P == 0:
        odd_cnt = 1
    else:
        odd_cnt = 0
else:
    odd_cnt = 2 ** (odd - 1)

print(odd_cnt * even_cnt)
