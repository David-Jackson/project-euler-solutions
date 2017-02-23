def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n / 10)


print "Answer:", sum_digits(2**1000)
