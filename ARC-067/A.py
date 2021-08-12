n = int(input())
MOD = 1000000007


def divisor(n):
    divs = []
    for i in range(2, n + 1):
        if n % i == 0:
            while n % i == 0:
                divs.append(i)
                n /= i

        if n == 1:
            return divs


dct = {}
for i in range(2, n + 1):
    for j in divisor(i):
        dct[str(j)] = dct.setdefault(str(j), 1) + 1

ans = 1
for k, v in dct.items():
    ans *= v
    ans %= MOD

print(ans)
