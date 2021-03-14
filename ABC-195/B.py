a, b, w = map(int, input().split())

ok = []

for i in range(10 ** 6 + 1):
    if a * i <= 1000 * w <= b * i:
        ok.append(i)

if len(ok) == 0:
    print("UNSATISFIABLE")
else:
    print(min(ok), max(ok))
