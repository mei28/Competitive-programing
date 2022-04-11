n = int(input())
S = list(input())

if S[0]!=S[-1]:
    print(1)
else:
    for i in range(n-1):
        if S[0] != S[i] and S[-1]!=S[i+1]:
            print(2)
            exit()

    print(-1)
        
