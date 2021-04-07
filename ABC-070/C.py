N = int(input())
T = [int(input()) for _ in range(N)]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


ans = 1

for t in T:
    ans = lcm(ans, t)
print(ans)
