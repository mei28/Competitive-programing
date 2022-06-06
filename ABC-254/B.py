import math

n = int(input())

for j in range(0, n):
    for i in range(0, j + 1):
        print(math.comb(j, i), end=" ")

    print()
