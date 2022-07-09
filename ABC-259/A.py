n, m, x, t, d = map(int, input().split())

hight = [0] * (m + 10)

a = 0
if x < n:
    a = abs(t - d * x)
else:
    a = abs(t - n * d)

hight[0] = a
for i in range(1, m + 2):
    if i <= x:
        hight[i] = hight[i - 1] + d
    else:
        hight[i] = hight[i-1]

print(hight[m])
