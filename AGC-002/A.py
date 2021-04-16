a, b = map(int, input().split())

if a <= 0 <= b:
    print("Zero")
    exit()
elif b <= 0:
    ab = abs(a - b)
else:
    ab = abs(a)

if ab % 2 == 1:
    print("Positive")
else:
    print("Negative")
