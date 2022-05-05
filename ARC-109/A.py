a, b, x, y = map(int, input().split())

y_ = min(y, x + x)

a = 2 * a
b = 2 * b + 1

d = abs(a - b)

print(d // 2 * y_ + d % 2 * x)
