K = int(input())
dct = dict()

for p in range(2, 10**6):
    if K % p != 0:
        continue
    dct[p] = 0
    while K % p == 0:
        dct[p] += 1
        K //= p

if K != 1:
    dct[K] = 1
ans = 0


def need(p, n):
    bot, top = 0, n * p

    while top - bot > 1:
        mid = bot + (top - bot) // 2
        x = mid
        res = 0
        while x:
            res += x // p
            x //= p
        if res >= n:
            top = mid
        else:
            bot = mid
    return top


for k, v in dct.items():
    ans = max(ans, need(k, v))
print(ans)
