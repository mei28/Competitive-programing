N, Y = map(int,input().split())

for i in range(N+1):
    for j in range(N-i+1):
        k = N - i - j
        _sum = 10000*i+5000*j+1000*k
        if _sum == Y:
            print(i,j,k)
            exit()
print(-1,-1,-1)
