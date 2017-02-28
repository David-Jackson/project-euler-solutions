def digits(n):
    d = []
    while n > 0:
        d.append(n % 10)
        n /= 10
    return d


def same_digits(a, b):
    ad = digits(a)
    bd = digits(b)
    if len(ad) != len(bd):
        return False
    ad.sort()
    bd.sort()
    return ad == bd


def all_same(i):
    for m in range(6, 1, -1):
        if not same_digits(i, i * m):
            return False
    return True

i = 1

while True:
    if all_same(i):
        print "Answer:", i
        break
    i += 1
