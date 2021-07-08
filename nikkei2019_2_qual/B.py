from typing import Counter

n = int(input())
D = list(map(int, input().split()))
MOD = 998244353

if D[0] != 0 or 0 in D[1:]:
    print(0)
else:
    cnter = Counter(D)
    result = 1

    for i in range(1, max(D) + 1):
        if cnter[i] == 0:
            print(0)
            exit()

        result = (result * pow(cnter[i - 1], cnter[i], MOD)) % MOD
    print(result)
