print(297)
ans_1 = [i for i in range(1, 100)]
ans_2 = [i * 100 for i in range(1, 100)]
ans_3 = [i * 10000 for i in range(1, 100)]

ans_1.extend(ans_2)
ans_1.extend(ans_3)

ans_1.sort()
print(*ans_1)
