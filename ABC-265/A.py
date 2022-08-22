x, y, n = map(int, input().split())

three = min(x * 3, y)

print(three * (n // 3) + x * (n % 3))
