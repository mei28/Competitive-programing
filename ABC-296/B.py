S = [input() for _ in range(8)]

alp = "abcdefgh"
num = "87654321"

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(alp[j] + num[i])
            exit()
