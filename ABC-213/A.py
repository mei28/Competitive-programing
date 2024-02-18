# 入力a,bとして a xor c =b となるcを求める関数を作成する
def xor(a, b):
    return a ^ b


# 数字a,b を入力から代入する
a, b = map(int, input().split())

# 関数xorにa,bを渡してcを出力する
print(xor(a, b))
