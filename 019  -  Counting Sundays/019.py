import datetime

cur = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
time_delta = datetime.timedelta(1)

count = 0

while cur < end:
    if (cur.day == 1 and cur.weekday() == 6):
        count += 1
    cur += time_delta

print "Answer:", count
