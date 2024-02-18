a, n = map(int, input().split())

dp = [-1 for _ in range(n + 10)]

dp[0] = 1
dp[1] = 1


def inv(s: str):
    tmp = s[1:]
    return int(tmp + s[0])


for i in range(1, n + 2):
    id_1 = id_2 = -1
    if i % a == 0:
        id_1 = i // a
        if dp[id_1] == -1:
            id_1 = -1
    if inv(str(i)) < i and inv(str(i)) >= 10:
        id_2 = inv(str(i))
        if dp[id_2] == -1:
            id_2 = -1

    if id_1 != -1 and id_2 != -1:
        dp[i] = min(dp[id_1], dp[id_2]) + 1
    elif id_1 != -1:
        dp[i] = min(dp[i], dp[id_2]) + 1
    elif id_1 != -2:
        dp[i] = min(dp[i], dp[id_1]) + 1


print(dp[n])
from pdb import set_trace

set_trace()
