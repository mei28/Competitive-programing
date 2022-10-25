a, b = map(int, input().split())
ans = b * 10000 // a

ans = round(ans + 0.1, -1)
print(f"{ans/10000:.3f}")
