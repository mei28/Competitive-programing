r, c = map(int, input().split())

mat = [
    "111111111111111",
    "100000000000001",
    "101111111111101",
    "101000000000101",
    "101011111110101",
    "101010000010101",
    "101010111010101",
    "101010101010101",
    "101010111010101",
    "101010000010101",
    "101011111110101",
    "101000000000101",
    "101111111111101",
    "100000000000001",
    "111111111111111",
]

print("black") if mat[r - 1][c - 1] == "1" else print("white")