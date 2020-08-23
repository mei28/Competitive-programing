H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())

matrix = [0 for _ in range(H)]
for i in range(H):
    input_line = list(input().split(""))
    matrix[i] = input_line
print(matrix[0])
