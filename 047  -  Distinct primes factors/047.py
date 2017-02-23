REQ_FACTOR_LENGTH = 4
REQ_STREAK = 4

cur_streak = 0
n = 3


def distinct_prime_factors(n):
    d = 2
    res = []
    while n > 1:
        if (n % d == 0):
            if (d not in res):
                res.append(d)
            n /= d
            d -= 1
        d += 1
    return res


while (cur_streak < REQ_STREAK):
    if (len(distinct_prime_factors(n)) == REQ_FACTOR_LENGTH):
        cur_streak += 1
    else:
        cur_streak = 0
    n += 1
    if (n % 1000 == 0):
        print "{0}\r".format(n),
print

for i in range(n - REQ_STREAK, n):
    print i, "-", distinct_prime_factors(i)

print "Answer:", n - REQ_STREAK
