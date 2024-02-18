n = int(input())

ans = 0


# A+B = N
# A+B = N
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


D = [0] * (n + 1)

for i in range(1, n + 1):
    D[i] = len(make_divisors(i))

ans = 0
for a in range(1, n + 1):
    m = n - a
    ans += D[a] * D[m]
print(ans)
# ans *= 2
# if n % 2 == 0:
#     ans += D[n // 2] * D[n - n // 2]
# print(ans)
