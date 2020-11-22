N = int(input())
S = input()

T = []
cnt = 0
for s in S:
    T.append(s)

    if T[-3:] == ['f', 'o', 'x']:
        T.pop()
        T.pop()
        T.pop()
        cnt += 1

print(N-3*cnt)
