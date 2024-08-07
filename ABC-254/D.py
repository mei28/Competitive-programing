n = int(input())


par = []
for i in range(1, n + 1):
    par.append(i * i)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def sum_(r, i):
    ans = 1
    if i == 1:
        return 1

    for _, j in r:
        ans *= j + 1
    return ans


ans = 0
for i in par:
    ret = factorization(i)
    ans += sum_(ret, i)

print(ans)
