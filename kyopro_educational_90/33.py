H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
    exit()

h = -(-H // 2)
w = -(-W // 2)
print(h * w)
