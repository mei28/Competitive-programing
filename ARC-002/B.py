from datetime import datetime, timedelta

formatter = "%Y/%m/%d"

date = datetime.strptime(input(), formatter)

while True:
    y, m, d = date.year, date.month, date.day
    if y % (m * d) == 0:
        break
    date += timedelta(days=1)

ans = date.strftime(formatter)
print(ans)
