class WD:
    # keyからvalueもvalueからkeyも計算量1で
    # アクセスできる辞書
    # 例 key:リンゴ,value:apple
    def __init__(self):
        self.Dict1 = {}
        self.Dict2 = {}

    def print(self):
        print("D1", self.Dict1)
        print("D2", self.Dict2)

    def set(self, value1, value2):
        # keyとvalueを入力(set(リンゴ,apple))
        self.Dict1[value1] = value2
        self.Dict2[value2] = value1

    def retvalue1(self, value1):
        # keyを入力するとvalue変換(retvalue1(リンゴ)→apple)
        return self.Dict1[value1]

    def retvalue2(self, value2):
        # valueを入力するとkey変換
        return self.Dict2[value2]

    def changevalue1(self, changed_value1, value2):
        # keyの方を変更したい時に、valueをもとに変更
        del self.Dict1[self.Dict2[value2]]
        self.Dict1[changed_value1] = value2
        self.Dict2[value2] = changed_value1

    def changevalue2(self, value1, changed_value2):
        # valueを変更したい時に、keyをもとに変更
        del self.Dict2[self.Dict1[value1]]
        self.Dict2[changed_value2] = value1
        self.Dict1[value1] = changed_value2

    def shiftvalue1(self, value1_1, value1_2):
        self.Dict2[self.Dict1[value1_1]], self.Dict2[self.Dict1[value1_2]] = (
            self.Dict2[self.Dict1[value1_2]],
            self.Dict2[self.Dict1[value1_1]],
        )
        self.Dict1[value1_1], self.Dict1[value1_2] = (
            self.Dict1[value1_2],
            self.Dict1[value1_1],
        )

    def shiftvalue2(self, value2_1, value2_2):
        self.Dict1[self.Dict2[value2_1]], self.Dict1[self.Dict2[value2_2]] = (
            self.Dict1[self.Dict2[value2_2]],
            self.Dict1[self.Dict2[value2_1]],
        )
        self.Dict2[value2_1], self.Dict2[value2_2] = (
            self.Dict2[value2_2],
            self.Dict2[value2_1],
        )

    def getsets(self):
        return set(self.Dict1.keys()), set(self.Dict2.keys())

    def delete_(self, value1):
        del self.Dict1[value1]
        del self.Dict2[value1]


n = int(input())
S = []
T = []
dct = WD()
for _ in range(n):
    s, t = input().split()
    S.append(s)
    T.append(t)
    dct.set(s, t)

S = set(S)
T = set(T)
if S == T:
    print("No")
else:
    # print("Yes")
    cnt = 0
    while cnt < 100:
        left, right = dct.getsets()
        right_keys = right - left
        if len(right_keys) == 0:
            break
        for k in right_keys:
            dct.changevalue1(k, k)
            dct.delete_(k)
        cnt += 1
    left, right = dct.getsets()

    if len(left) > 0 and left == right:
        print("No")
    else:
        print("Yes")

"""NG
5
aaa bbb
yyy zzz
ccc aaa
xxx yyy
bbb ccc
"""

"""ok
5
aaa bbb
yyy zzz
ccc ddd
xxx yyy
bbb ccc
"""
