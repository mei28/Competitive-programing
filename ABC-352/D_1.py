N, K = map(int, input().split())
P = list(map(int, input().split()))


# pos[v] will store the index position of value v in P (1-based index)
pos = [0] * (N + 1)

for i in range(N):
    pos[P[i]] = i + 1

import sys
from collections import deque

min_diff = sys.maxsize

# We'll use a deque to find the minimum and maximum efficiently in a sliding window
# These deques store indices in the range [1...N] referring to pos
min_deque = (
    deque()
)  # this will store indices of the 'pos' array such that values are in increasing order
max_deque = (
    deque()
)  # this will store indices of the 'pos' array such that values are in decreasing order

# We consider windows of values [a, a+1, ..., a+K-1]
# and we need to check pos[a], pos[a+1], ..., pos[a+K-1]
for a in range(1, N - K + 2):
    # Current window of values is from a to a+K-1 (inclusive)
    # We add a+K-1 to the deques
    current = a + K - 1

    # Remove elements out of this range
    if min_deque and min_deque[0] < a:
        min_deque.popleft()
    if max_deque and max_deque[0] < a:
        max_deque.popleft()

    # Maintain min deque
    while min_deque and pos[min_deque[-1]] >= pos[current]:
        min_deque.pop()
    min_deque.append(current)

    # Maintain max deque
    while max_deque and pos[max_deque[-1]] <= pos[current]:
        max_deque.pop()
    max_deque.append(current)

    # If we have a full window [a, a+1, ..., a+K-1]
    if a >= 1 and current == a + K - 1:
        # The minimum value in pos within range [a, a+K-1]
        min_pos = pos[min_deque[0]]
        # The maximum value in pos within range [a, a+K-1]
        max_pos = pos[max_deque[0]]
        # Calculate the index difference
        diff = max_pos - min_pos
        # Update minimum difference found
        min_diff = min(min_diff, diff)

# Output the minimal index difference for any valid sequence
print(min_diff)
