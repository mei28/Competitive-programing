n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

if n < m:
    print("NO")
    exit()


flg = True
for i in range(m):
    if A[i] < B[i]:
        flg = False
        break

if flg:
    print("YES")
else:
    print("NO")
