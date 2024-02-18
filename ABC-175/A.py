S = input()

cnt = S.count("R")
if cnt == 1:
    print(cnt)
elif cnt == 0:
    print(cnt)
elif cnt == 3:
    print(cnt)
else:
    if S[1] == "S":
        print(1)
    else:
        print(cnt)
