R, G, B, N = map(int, input().split())


# Rr+Gg+Bb=N s.t. (r,g,b)

ans = 0

for r in range(0, -(-N // R) + 1):
    for g in range(0, -(-(N - r) // G) + 1):
        if R * r + G * g > N:
            continue
        diff = N - R * r - G * g
        if diff % B != 0:
            continue
        ans += 1

print(ans)
