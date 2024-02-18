import sys


def main(lines):
    timeline = []
    distance = []
    for i in lines:
        t, d = i.split(" ")
        timeline.append(t)
        d = float(d)
        distance.append(d)

    sum_dist = 0.0
    for t, d in zip(timeline, distance):
        h, m, s = map(float, t.split(":"))
        if h % 24 >= 22 or h % 24 <= 4:
            sum_dist += d * 1.25

        else:
            sum_dist += d
    if sum_dist <= 1052:
        print(410)
    else:
        print(int(-(-(sum_dist - 1052) // 237) * 80 + 410))


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)


################################################################


def main(lines):
    timeline = []
    distance = []
    for i in lines:
        t, d = i.split(" ")
        timeline.append(t)
        d = float(d)
        distance.append(d)

    sum_dist = 0.0
    sum_delay_time = 0
    old_m, old_s = 0.0, 0.0
    old_dist = 0.0
    for t, d in zip(timeline, distance):
        h, m, s = map(float, t.split(":"))
        diff_dist = abs(d - old_dist)
        diff_sec = abs((m * 60 + s) - (old_m * 60 + old_s))
        if diff_sec == 0:
            sum_delay_time += diff_sec
        elif (diff_dist / 1000) / (diff_sec / (60 * 60)) < 10:
            sum_delay_time += diff_sec
        if h % 24 >= 22 or h % 24 <= 4:
            sum_dist += d * 1.25
        else:
            sum_dist += d
        old_m, old_s = m, s
        old_dist = d

    delay_fare = -(-sum_delay_time // 90) * 80
    if sum_dist <= 1052:
        print(int(410 + delay_fare))
    else:
        print(int(-(-(sum_dist - 1052) // 237) * 80 + 410 + delay_fare))


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
