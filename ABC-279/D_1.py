a, b = map(int, input().split())


def f(n):
    return n * b + a / ((n + 1) ** (0.5))


l = ((a / (2 * b)) ** 2) ** (1 / 3)
min_ans = f(0)

l = int(l)
for i in range(-10, 10):
    n = i + l
    if n < 0:
        continue
    min_ans = min(min_ans, f(n))
print(min_ans)
