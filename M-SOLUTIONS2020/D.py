n = int(input())
A = [int(x) for x in input().split()]
# 最初の所持金
money = 1000
# 所有株数
kabu_c = 0
# 予言で翌日上がるかどうかのリスト
l = list()
for i in range(n-1):
    if A[i+1] - A[i] > 0:
        l.append(1)
    else:
        l.append(0)
for idx, i in enumerate(l):
    # 翌日上がってかつその時の株価で買える所持金があるなら買う。
    if i == 1 and money - A[idx] >= 0:
        kabu_c = money // A[idx]
        money = money - (kabu_c * A[idx])
    # 翌日上がらないなら売っちゃう（その時点での利幅ゲット）
    if i == 0:
        money = money + (kabu_c * A[idx])
        kabu_c = 0
# 上がり調子だと最終日で売り切ってない可能性があるので所持している株は最終日で売り切る
if kabu_c > 0:
    money = money + (kabu_c * A[n-1])
print(money)
