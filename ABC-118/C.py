N = int(input())
A = list(map(int, input().split()))


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


ans = A[0]

for a in A:
    ans = gcd(a, ans)

print(ans)
