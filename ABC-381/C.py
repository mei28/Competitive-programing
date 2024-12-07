N = int(input())
S = input()

l1 = [0] * N
if S[0] == '1':
    l1[0] = 1
for i in range(1, N):
    if S[i] == '1':
        l1[i] = l1[i-1] + 1
    else:
        l1[i] = 0

r2 = [0] * N
if S[N-1] == '2':
    r2[N-1] = 1
for i in range(N-2, -1, -1):
    if S[i] == '2':
        r2[i] = r2[i+1] + 1
    else:
        r2[i] = 0

max_length = 0
for i in range(N):
    if S[i] == '/':
        left_ones = l1[i-1] if i > 0 else 0
        right_twos = r2[i+1] if i+1 < N else 0
        k = min(left_ones, right_twos)
        length = 1 + 2 * k
        if length > max_length:
            max_length = length

print(max_length)

