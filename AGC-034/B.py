S = input()

cnt_a = 0
ans = 0
for i in range(0,len(S)-1):
    if S[i] == 'A':
        cnt_a +=1

    elif S[i:i+2]=="BC":
        ans += cnt_a

    elif i>0 and S[i-1:i+1] == "BC":
        continue

    else:
        cnt_a = 0

print(ans)
