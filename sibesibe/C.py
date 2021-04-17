x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
x_0, y_0 = x_b - x_a, y_b - y_a
x_1, y_1 = x_c - x_a, y_c - y_a

s = abs(x_0 * y_1 - y_0 * x_1) / 2
print(s)
