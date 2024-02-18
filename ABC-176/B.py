N = input()

tmp = 0
for i in N:
    i = int(i)
    tmp = (tmp + i) % 9

if tmp == 0:
    print("Yes")
else:
    print("No")
