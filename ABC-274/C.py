n = int(input())
A = list(map(int, input().split()))

# dp = [-1] * (10**6)
dct = {}

S = set()

for a in A:
    S.add(a)
    S.add(2 * a + 1)
    S.add(2 * a)

S = list(S)
S.sort()

for s in S:
    cnt = 0
    s_ = s
    while s > 0:
        cnt += 1
        s = s >> 1
    dct[s_] = cnt - 1

print(0)
for a in A:
    print(dct[2 * a])
    print(dct[2 * a + 1])
