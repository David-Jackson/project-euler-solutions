def digit_sum(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum(int(n / 10))


maxA = 1
maxB = 1
max = 1

for a in range(100):
    for b in range(100):
        s = digit_sum(a**b)
        if (max < s):
            maxA = a
            maxB = b
            max = s


print "Answer:", "a =", maxA, "b =", maxB, "sum =", max
