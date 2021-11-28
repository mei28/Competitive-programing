n = int(input())
S = input()

def rls(S):
    tmp,count,ans = S[0],1,0

    for i in range(1,len(S)):
        if tmp == S[i]:
            count+=1
        else:
            ans += count*(count-1)//2
            tmp = S[i]
            count=1
    
    ans += count*(count-1)//2
    return ans

l = rls(S)
print(l)
