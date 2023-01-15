n, k = map(int, input().split())
k -= (n - 1) * 2

if k < 0:
    print("No")
elif k % 2 == 0:
    print("Yes")
else:
    print("No")
