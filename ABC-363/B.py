n, t, p = map(int, input().split())
Ls = list(map(int, input().split()))

Ls.sort()
current_T_or_more = sum(1 for length in Ls if length >= t)

if current_T_or_more >= p:
    print(0)
    exit()

days_needed = 0
while current_T_or_more < p:
    days_needed += 1
    current_T_or_more = sum(1 for length in Ls if length + days_needed >= t)

print(days_needed)
