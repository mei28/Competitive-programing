import bisect

W, H = map(int, input().split())
N = int(input())
strawberries = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
cuts_x = list(map(int, input().split()))
B = int(input())
cuts_y = list(map(int, input().split()))

cuts_x = [0] + cuts_x + [W]
cuts_y = [0] + cuts_y + [H]
cuts = [cuts_x, cuts_y]

# Create list of ranges for x and y
x_ranges = list(zip(cuts_x[:-1], cuts_x[1:]))
y_ranges = list(zip(cuts_y[:-1], cuts_y[1:]))

# Initialize counter
counter = [[0 for _ in y_ranges] for _ in x_ranges]

# Count strawberries
ans = set()
for x, y in strawberries:
    # Find the position of the strawberry
    pos_x = bisect.bisect(cuts_x, x) - 1
    pos_y = bisect.bisect(cuts_y, y) - 1
    # Increase the counter
    counter[pos_x][pos_y] += 1
    ans.add(counter[pos_x][pos_y])

if N < (A + 1) * (B + 1):
    ans.add(0)

print(min(ans), max(ans))
