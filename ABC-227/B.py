from collections import Counter

n = int(input())
S = list(map(int,input().split()))

cnt = Counter(S)

ans = 0
for s,k in cnt.items():
    flg =False 
    for a in range(1,1000):
        for b in range(1,1000):
            if 4*a*b + 3*a+ 3*b==s:
                ans += k
                flg =True
                break
        
        if flg:
            break

print(n-ans)
            
        

