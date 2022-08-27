L, X, Y, S, D = map(int, input().split())

if D < S:
    D += L

ans = (D - S) / (X + Y)
if X < Y:
    ans = min(ans, ((L - D + S) / (Y - X)))

print(ans)
