n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

canvas = [["."]*(s-r+1) for _ in range(q-p+1)]

dh = [i-a for i in range(p,q+1)]
dw = [i-b for i in range(r,s+1)]

for i in range(q-p+1):
    for j in  range(s-r+1):
        _w,_h = dw[j],dh[i]
        if abs(_w)==abs(_h):
            canvas[i][j] = "#"


for c in canvas:
    print(''.join(c))
