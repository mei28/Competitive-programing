n = int(input())
lst0 = list(map(int, input().split()))
lst1 = [0, 0, 0, 0, 0, 0, 0, 0]
god = 0
Mx, Mn = (0, 0)
for i in range(n):
    if 1 <= lst0[i] <= 399:
        lst1[0] += 1
    elif 400 <= lst0[i] <= 799:
        lst1[1] += 1
    elif 800 <= lst0[i] <= 1199:
        lst1[2] += 1
    elif 1200 <= lst0[i] <= 1599:
        lst1[3] += 1
    elif 1600 <= lst0[i] <= 1999:
        lst1[4] += 1
    elif 2000 <= lst0[i] <= 2399:
        lst1[5] += 1
    elif 2400 <= lst0[i] <= 2799:
        lst1[6] += 1
    elif 2800 <= lst0[i] <= 3199:
        lst1[7] += 1
    else:
        god += 1

Mn = 8 - lst1.count(0)
Mx = Mn + god
if Mn == 0:
    Mn = 1
print(str(Mn) + " " + str(Mx))
