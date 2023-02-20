w, h, n = map(int, input().split())

w_min, w_max = 0, w
h_min, h_max = 0, h

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        w_min = max(w_min, x)
    if a == 2:
        w_max = min(w_max, x)
    if a == 3:
        h_min = max(h_min, y)
    if a == 4:
        h_max = min(h_max, y)

if w_max - w_min < 0 or h_max - h_min < 0:
    print("0")
else:
    print((w_max - w_min) * (h_max - h_min))
