from math import factorial


def fact_digits_sum(n):
    sum = 0
    while n > 0:
        sum += factorial(n % 10)
        n /= 10
    return sum


def fact_chain_len(n):
    hist = []
    while n not in hist:
        hist.append(n)
        n = fact_digits_sum(n)
    return len(hist)


count = 0
for i in range(2, 1000000):
    if fact_chain_len(i) == 60:
        count += 1
        print "{0}, {1}\r".format(i, count),

print "Answer:", count
