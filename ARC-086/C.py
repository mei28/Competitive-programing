N, K = map(int, input().split())
A = list(map(int, input().split()))

dct = {}
key_set = set()
for a in A:
    dct[a] = dct.setdefault(a, 0) + 1
    key_set.add(a)

dct = sorted(dct.items(), key=lambda x: x[1])

diff_n = len(key_set) - K

if diff_n <= 0:
    print(0)

else:
    ans = 0
    for i in range(diff_n):
        ans += dct[i][1]
    print(ans)
