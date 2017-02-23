div = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 20


def div_all(x):
    for y in div:
        if (x % y != 0):
            return False
    return True


while (True):
    if (div_all(i)):
        break
    i += 20

print "Answer:", i
