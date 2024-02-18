import math

N, M = map(int, input().split())

if M == 0:
    print(N)
    exit()

H = [1] * N
A = list(map(int, input().split()))
for a in A:
    H[a - 1] = 0

if M == N:
    print(0)
    exit()

ren = 0
rens = []

for h in H:
    if h == 1:
        ren += 1
    else:
        if ren != 0:
            rens.append(ren)
        ren = 0

if ren != 0:
    rens.append(ren)

if len(rens) == 0:
    print(0)
    exit()

stride = min(rens)
ans = 0
for a in rens:
    ans += math.ceil(a / stride)

print(ans)
