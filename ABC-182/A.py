a, b = map(int, input().split())

diff = 2 * a + 100

print(max(diff-b,0))
