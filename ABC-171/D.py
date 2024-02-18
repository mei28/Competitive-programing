from collections import Counter

n = int(input())
A = list(map(int, input().split()))

q = int(input())
cnter = Counter(A)
ans = sum(A)
for _ in range(q):
    b, c = map(int, input().split())
    if b not in cnter.keys():
        cnter[b] = 0
    if c not in cnter.keys():
        cnter[c] = 0
    cnt_b = cnter[b]
    cnt_c = cnter[c]

    ans -= b * cnter[b]
    tmp = cnter[b]
    cnter[b] = 0
    cnter[c] += tmp
    ans += c * tmp
    print(ans)
