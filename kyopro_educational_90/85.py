k = int(input())

primers = []

for i in range(1, int(k ** 0.5) + 1):
    if k % i != 0:
        continue
    primers.append(i)
    if i != k // i:
        primers.append(k // i)

ans = 0

for i in range(len(primers)):
    for j in range(i, len(primers)):
        a, b = primers[i], primers[j]
        c = 0
        if k % (a * b) != 0:
            continue
        c = k / (a * b)
        if b <= c:
            ans += 1

print(ans)
