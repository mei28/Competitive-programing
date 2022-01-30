h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]

ans = []
for i in range(w):
    tmp = []
    for j in range(h):
        tmp.append(A[j][i])
    ans.append(tmp)

for i in ans:
    print(*i)
        

