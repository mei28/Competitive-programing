def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


A, B, C, D = map(int, input().split())

b_num = B // C + B // D - B // (lcm(C, D))
a_num = (A - 1) // C + (A - 1) // D - (A - 1) // (lcm(C, D))

print((B - A + 1) - (b_num - a_num))
