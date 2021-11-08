n = int(input())

dct:dict = {}
for i in range(n):
    line = list(map(int,input().split()))
    l = line[0]
    ll = ''
    for j in line[1:]:
        ll += str(j)+ ','
    dct.setdefault(str(l),set()).add(ll)


ans = 0
# print(dct)
for k,v in dct.items():
    ans += len(v) 


print(ans)
        
