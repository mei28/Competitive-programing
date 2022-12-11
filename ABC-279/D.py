a, b = map(int, input().split())


def f(n):
    return n * b + a / ((n + 1) ** (0.5))


l, r = 0, 10**18
while l + pow(10, -2) < r:
    c1 = l + (r - l) / 3
    c2 = r - (r - l) / 3

    if f(c1) < f(c2):
        r = c2
    else:
        l = c1
min_ans = f(0)

l = int(l)
for i in range(-10, 10):
    n = i + l
    if n < 0:
        continue
    min_ans = min(min_ans, f(n))
print(min_ans)
