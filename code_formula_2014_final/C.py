message = list(map(str, input().split(" ")))
message2 = [s for s in message if ("@" in s)]  # @を含む要素を抽出
mention = []
mention_user = []
for s in message2:
    mention = s.split("@")  # 各要素を@で分割
    mention.pop(0)  # 先頭の''を削除
    for m in mention:  # 重複を省いてリストに追加
        if (m in mention_user) == False and m != "":
            mention_user.append(m)


mention_user.sort()

for m in mention_user:
    print(m)
