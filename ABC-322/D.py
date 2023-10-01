def rotate(polyomino):
    return ["".join(row) for row in zip(*polyomino[::-1])]

def all_rotations(polyomino):
    rotations = [polyomino]
    for _ in range(3):
        polyomino = rotate(polyomino)
        if polyomino not in rotations:
            rotations.append(polyomino)
    return rotations

def can_place(board, polyomino, x, y):
    for i in range(len(polyomino)):
        for j in range(len(polyomino[0])):
            if polyomino[i][j] == "#":
                if x + i >= 4 or y + j >= 4 or x + i < 0 or y + j < 0:
                    return False
                if board[x + i][y + j] == "#":
                    return False
    return True

def place(board, polyomino, x, y):
    for i in range(len(polyomino)):
        for j in range(len(polyomino[0])):
            if polyomino[i][j] == "#":
                board[x + i][y + j] = "#"
    return board

def unplace(board, polyomino, x, y):
    for i in range(len(polyomino)):
        for j in range(len(polyomino[0])):
            if polyomino[i][j] == "#":
                board[x + i][y + j] = "."
    return board

def solve(board, polyominoes):
    if not polyominoes:
        return all(cell == "#" for row in board for cell in row)

    polyomino = polyominoes[0]
    for x in range(-3, 4): 
        for y in range(-3, 4):  
            for rotated in all_rotations(polyomino):
                if can_place(board, rotated, x, y):
                    new_board = [row.copy() for row in board]
                    place(new_board, rotated, x, y)
                    if solve(new_board, polyominoes[1:]):
                        return True
    return False

polyominoes = []
for _ in range(3):
    polyomino = [input().strip() for _ in range(4)]
    polyominoes.append(polyomino)

grid = [["." for _ in range(4)] for _ in range(4)]
if solve(grid, polyominoes):
    print("Yes")
else:
    print("No")

