l,r = map(int,input().split())

w = r-l

def gcd(a,b)->int:
    if b==0:
        return a
    else:
        return gcd(b,a%b)

while w>0:
    for x in range(l,r-w+1):
        y = x+w
        if gcd(x,y)==1:
            print(w)
            exit()
            


