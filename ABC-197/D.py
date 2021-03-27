import math

import numpy as np

N = int(input())


def rotation_o(u, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

    return np.dot(R, u)


def rotation(xy, r_axis, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    xy = np.array(xy)
    r_axis = np.array(r_axis)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

    return np.dot(R, xy - r_axis) + r_axis


x0, y0 = map(int, input().split())
x_n2, y_n2 = map(int, input().split())

x_, y_ = ((x0 + x_n2) / 2, (y0 + y_n2) / 2)

p = (x_, y_)

q = (x0, y0)

ans = rotation(q, p, 2 * np.pi / N)
print(ans[0], ans[1])
