n = int(input())
A = list(map(int, input().split()))
B = [[0] * 3 for _ in range(n)]


def get_nisan(a):
    ni, san = 0, 0

    while a % 2 == 0:
        ni += 1
        a /= 2

    while a % 3 == 0:
        san += 1
        a /= 3
    return ni, san, int(a)


for i, a in enumerate(A):
    ni, san, b = get_nisan(a)
    B[i][0] = ni
    B[i][1] = san
    B[i][2] = b

tmp = set()
for b in B:
    tmp.add(b[2])

if len(tmp) > 1:
    print(-1)
    exit()

ans = 0
nii = 10**9
sann = 10**9
for b in B:
    nii = min(nii, b[0])
    sann = min(sann, b[1])
for b in B:
    ans += (b[0] - nii) + (b[1] - sann)
print(ans)
