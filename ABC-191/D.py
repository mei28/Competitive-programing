import math

X, Y, R = map(float, input().split())

X_right = math.floor(X+R)
X_left = math.ceil(X-R)

cnt = 0

for i in range(X_left, X_right+1, 1):
    p = math.sqrt(R**2-(X-i)**2)
    p_top = math.floor(p+Y)
    p_bottom = math.ceil(Y-p)

    cnt += (p_top-p_bottom)+1

print(cnt)
