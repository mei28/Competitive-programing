import math

N = int(input())

ans = 2


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


for i in range(2, N + 1):
    ans = lcm(ans, i)
print(ans + 1)
