N = int(input())
X = list(map(int, input().split()))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
primes_set = set()

for x in X:
    for p in primes:
        if x % p == 0:
            primes_set.add(p)
            break

ans = 1
for i in list(primes_set):
    ans *= i

print(ans)
