h, w = map(int, input().split())
S = [input() for _ in range(h)]

cnt = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if S[i][j] == "#":
            if S[i-1][j] == '#' and S[i+1][j] == '#' and S[i][j-1] == '#' and S[i][j+1] == '#':
                cnt +=1 
print(cnt)
