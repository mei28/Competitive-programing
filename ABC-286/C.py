n, a, b = map(int, input().split())

S = input()
T = S + S


def check(tmp):
    ret = 0
    for i in range(n // 2):
        if tmp[i] != tmp[-(i + 1)]:
            ret += b

    # print(tmp, ret)
    return ret


ans = 1 << 60

for i in range(n):
    tmp = T[i : i + n]
    ret = check(tmp)
    ans = min(i * a + ret, ans)
print(ans)
