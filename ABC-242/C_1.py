n = int(input())
MOD = 998244353

if n == 1:
    print(9)
    exit()


cnt = 9
for i in range(1, n):
    sita = 2 ** (i - 1)
    ue = cnt - sita

    cnt = ue * 3 + sita * 2
    cnt %= MOD

print(cnt)
