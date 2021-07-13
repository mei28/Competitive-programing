a, b = map(int, input().split())
if b - a < 0:
    print(0)
else:
    print(b - a + 1)
