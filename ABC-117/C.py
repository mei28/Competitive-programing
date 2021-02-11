n,m = map(int,input().split())
x = list(map(int,input().split()))

x.sort()
diff = []

if n>=m:
    print(0)
    exit()

ans = 0

for i in range(1,len(x)):
    diff.append(abs(x[i]-x[i-1]))
    ans += abs(x[i]-x[i-1])

diff.sort(reverse=True)

for i in range(n-1):
    ans -= diff[i] 

print(ans)
    
