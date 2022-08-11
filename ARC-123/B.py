n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

ans = 0

while A:
    a = A.pop()
    b = 0
    while B and a >= b:
        b = B.pop()

    if not B and a >= b:
        break

    c = 0

    while C and b >= c:
        c = C.pop()

    if not C and b >= c:
        break

    ans += 1

print(ans)
