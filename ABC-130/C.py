W, H, x, y = map(int, input().split())


print("{:10f}".format(W * H / 2), end=" ")
if x * 2 == W and y * 2 == H:
    print(1)
else:
    print(0)
