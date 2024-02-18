import math

a, b = map(int, input().split())

d = a**2 + b**2


print(a / math.sqrt(d), b / math.sqrt(d))
