s = input()
# 両端から見て同じならカウントを進める，どっちかにxだったら追加,それ以外はだめ

left = 0
right = len(s) - 1

ans = 0
while left < right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        if s[left] == "x":
            left += 1
            ans += 1
        elif s[right] == "x":
            right -= 1
            ans += 1
        else:
            ans = -1
            break

print(ans)
