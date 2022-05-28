import math

n, a, b = map(int, input().split())

S = (1 + n) * n // 2

da = n // a
Sa = (a + da * a) * da // 2
db = n // b
Sb = (b + db * b) * db // 2


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


lab = lcm(a, b)
dab = n // lab
Sab = (lab + lab * dab) * dab // 2

print(S + Sab - Sa - Sb)
