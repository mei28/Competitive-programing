import sys

with open(sys.argv[1], "r") as f:
    l = f.readlines()

a = list(map(int, l[0].split()))
N = len(a)
check = [0] * (N + 1)

for i in a:
    check[i - 1] = 1
print(check.index(0) + 1)
