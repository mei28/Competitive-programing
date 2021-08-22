n, m = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(max(A), m)

k = [True] * (maxA + 1)
isPrime = [True] * (maxA + 1)
prime = []

for a in A:
    k[a] = False

for i in range(2, maxA + 1):
    if not isPrime[i]:
        continue
    for j in range(i * 2, maxA + 1, i):
        isPrime[j] = False
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)


for p in prime:
    for j in range(p * 2, m + 1, p):
        k[j] = k[j] and k[p]

ans = [1]
for i in range(2, m + 1):
    if k[i]:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)
