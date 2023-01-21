val = {"R": 1, "B": 2, "W": 0}

n, c = input().split()
A = input()
B = sum(map(lambda x: val[x], A))

if B % 3 == val[c]:
    print("Yes")
else:
    print("No")
