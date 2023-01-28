n = int(input())
A = input()
B = input()
MOD = 998244353

C = ""
D = ""
for a, b in zip(A, B):
    if int(a) < int(b):
        a, b = b, a

    C += a
    D += b

C = int(C)
D = int(D)
print(C * D % MOD)
