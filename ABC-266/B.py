n = int(input())
A = 998244353

ans = n - A

ok = 0
ng = 10000000000

b = n // A

for i in range(-5, 5):
    c = b + i
    x = n - A * c
    if 0 <= x < A:
        print(x)
        exit()
