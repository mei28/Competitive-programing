a,b = map(int,input().split())

if a == 1:
    if b==2 or b==10:
        print("Yes")
    else:
        print('No')
elif b == 1:
    if a==2 or b==10:
        print("Yes")
    else:
        print('No')

else:
    if abs(a-b) == 1:
        print("Yes")
    else:
        print("No")
