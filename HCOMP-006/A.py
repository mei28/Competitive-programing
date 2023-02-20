n = int(input())
H = list(map(int, input().split()))


if n <= 2:
    print("Yes")
    exit()

for i in range(1, n):
    if H[i - 1] > H[i]:
        print("No")
        exit()
    else:
        if H[i] != H[i - 1]:
            H[i] -= 1
print("Yes")
