a, b, c = map(int, input().split())

if a != b and b != c and a != c:
    print(0)
elif a == b and a != c:
    print(c)
elif a == c and a != b:
    print(b)
elif b == c and a != b:
    print(a)
else:
    print(a)
