n = int(input())
A = list(map(int, input().split()))

B = []
C = set()
for a in A:
    # if a not in C:
    #     B.append(a)
    # if 2 * a not in C:
    #     B.append(2 * a)
    # if 2 * a + 1 not in C:
    #     B.append(2 * a + 1)
    #
    # C = set(B)
    if a == 1:
        B.append(1)
        B.append(2)
        B.append(3)
    else:
        B.append(2 * a)
        B.append(2 * a + 1)

for b in B:
    cnt = 0
    while b > 1:
        b = b >> 1
        cnt += 1
    print(cnt)
