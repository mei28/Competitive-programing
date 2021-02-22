import sys

x = [i for i in input()]
for nums in range(len(x)):
    if nums % 2 == 0 and x[nums] == x[nums].lower():
        continue
    if nums % 2 != 0 and x[nums] == x[nums].upper():
        continue
    else:
        print("No")
        sys.exit()
print("Yes")
