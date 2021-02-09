N = int(input())

H = list(map(int,input().split()))


res = 0

while True:
    if all([h==0 for h in H]):
        break


    i = 0
    while i<N:
        if H[i] == 0:
            i += 1
        else:
            res += 1 
            while i<N and H[i]>0:
                H[i] -= 1
                i += 1

print(res)

