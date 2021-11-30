n = int(input())

def div(n:int)->list:
    ans = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            ans.append(i)
            if n%i != i:
                ans.append(n//i)
    ans.sort()
    return ans


divs = div(n)
ans = 0
for i in divs:
    if i==1:
        continue
    i -= 1
    if n//i ==n%i:
        ans += i

print(ans)
