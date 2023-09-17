M = int(input())
S = [input() for _ in range(3)]

ans = 3 * M

for i in range(3 * M):
    for j in range(3 * M):
        for k in range(3 * M):
            # 3つのリールの文字がすべて一致する場合
            if S[0][i % M] == S[1][j % M] == S[2][k % M]:
                # 3つのリールを止めるためにボタンを押すのにかかる最大秒数を計算
                if i != j and j != k and k != i:
                    t = max(i, j, k)
                    ans = min(ans, t)

print(ans if ans != 3 * M else -1)
