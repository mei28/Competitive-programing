N = int(input())
S = input()
T = input()
if S ==T:
    print(N)
    exit()

ans = 2 *N
for i in range(0,N):
    if S[-i:] == T[:i]:
        ans = 2*N -i
print(ans)
