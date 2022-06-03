l, r = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for i in reversed(range(r - l + 1)):
    for j in range(l, r - i + 1):
        if gcd(i, j) == 1:
            print(i)
            exit()
