a,b,c,d = map(int, input().split())

if a <= c and c <= d and c <= b and b <= d:
    print("Yes")
elif a <= c and d <= b:
    print("Yes")
elif c <= a and b <= d:
    print("Yes")
elif c<=a and a<=d and a<=d and d<=b:
    print("Yes")
else:
    print("No")