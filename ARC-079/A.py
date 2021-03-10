N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

inter = set()
for a, b in ab:
    if a == 1:
        inter.add(b)

for a, b in ab:
    if a in inter and b == N:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
