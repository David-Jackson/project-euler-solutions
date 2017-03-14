def sq_digit_sum(n):
    sum = 0
    while n > 0:
        r = (n % 10)
        sum += (r * r)
        n /= 10
    return sum


def sq_digit_chain(n):
    while n != 1 and n != 89:
        n = sq_digit_sum(n)
        # yield n
    return n


count = 0
i = 1

while i < 10000000:
    if sq_digit_chain(i) == 89:
        count += 1
    i += 1
    print "{0} - {1}\r".format(i, count),

print 
print "Answer:", count
