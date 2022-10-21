N = int(input())
S = [input() for _ in range(2)]
MOD = 1000000007

ans = 1
x = 0
pre = -1

while x < N:
    # 縦の時
    if S[0][x] == S[1][x]:
        if pre < 0:
            ans = 3
        elif pre == 0:
            ans *= 2
        else:
            ans *= 1
        x += 1
        pre = 0
    else:
        if pre < 0:
            ans = 6
        elif pre == 0:
            ans *= 2
        else:
            ans *= 3
        x += 2
        pre = 1
    ans %= MOD
print(ans)
