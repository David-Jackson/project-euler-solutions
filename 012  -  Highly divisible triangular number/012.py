def factor_count(x):
    count = 0
    for i in range(1, int(x**0.5) + 1):
        if (x % i == 0):
            count += 1
            if (i != x / i):
                count += 1
    return count


def triangle_numbers():
    i = 1
    sum = 0
    while (True):
        sum += i
        i += 1
        yield sum


for tri in triangle_numbers():
    if factor_count(tri) > 500:
        print "Answer:", tri
        break
    print "{0}\r".format(tri),
