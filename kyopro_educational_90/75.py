n = int(input())
primes = dict()

for denominator in range(2, int(n**0.5) + 1):
    while n % denominator == 0:
        n //= denominator
        primes[denominator] = primes.setdefault(denominator, 0) + 1

if n != 1:
    primes[n] = primes.setdefault(n, 0) + 1

cnt = 0
for k, v in primes.items():
    cnt += v

if cnt == 1:
    print(0)
else:
    ans = 0
    while cnt > 1:
        ans += 1
        cnt = -(-cnt // 2)
    print(ans)
