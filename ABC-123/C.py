N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

mi = min(A, B, C, D, E)

ans = -(-N // mi)
print(ans + 4)
