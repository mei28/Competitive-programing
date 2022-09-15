n = int(input())
A = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = 0
for i in range(1, n):
    g = gcd(g, abs(A[i] - A[i - 1]))

print(2) if g == 1 else print(1)
