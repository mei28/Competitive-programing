n = int(input())
T = input()

if '111' in T or '000' in T:
    print(0)
    exit()
if T not in '110'*(n+10):
    print(0)
    exit()
if T=='1':
    print(2*10**10)
elif T =='11':
    print(10**10)
else:
    k = T.count('0')
    if T[-1]=='0':
        print(10**10-k+1)
    else:
        print(10**10-k)


