A, B = map(int, input().split())
S = input()

if len(S) != A + B + 1:
    print('No')
    exit()

if S[A ] != '-':
    print('No')
    exit()

for i in range(A + B + 1):
    s = S[i]
    if s == '-' and i != A:
        print('No')
        exit()

print("Yes")


