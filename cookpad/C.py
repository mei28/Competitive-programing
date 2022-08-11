# coding: utf-8
# Your code here!

import requests


def my_post(q: int):
    data = '{"minutes":' + str(q) + "}"
    response = requests.post(
        "https://r3k3audez7.execute-api.ap-northeast-1.amazonaws.com/Prod/coffeepot/",
        data=data,
    )
    return response.json()


def isRemaing(j) -> bool:
    if j["remaining"] == 0:
        return True
    else:
        return False


def returnZeroMin(start):
    j = my_post(start)

    if isRemaing(j):
        return j["minutes"]
    else:
        return returnZeroMin(min(start * 2, 180))


def binary_search(right):
    left = 0
    right = right
    while left <= right:
        mid = (left + right) // 2
        mid_remain = my_post(mid)
        if mid_remain["remaining"] > 0:
            left = mid + 1
        else:
            right = mid - 1

        if abs(right - left) < 1:
            return left
    return -1
