def swap(a, b):
    if a < b:
        a, b = b, a
    return a, b


ans = 0
A, B = map(int, input().split())
A, B = swap(A, B)
while B > 0:
    ans += A // B
    A %= B
    A, B = swap(A, B)

print(ans - 1)
