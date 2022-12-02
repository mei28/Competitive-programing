N = int(input())
(*S,) = map(int, input())
(*T,) = map(int, input())

count = len([1 for s, t in zip(S, T) if s != t])

if count % 2:
    print(-1)
    exit()

U = []
countS = count // 2
countT = count // 2
for s, t in zip(S, T):
    if s == t:
        U.append(0)
        continue
    if s == 0 and countS > 0:
        U.append(0)
        countS -= 1
    elif t == 0 and countT > 0:
        U.append(0)
        countT -= 1
    else:
        U.append(1)

print("".join(map(str, U)))
