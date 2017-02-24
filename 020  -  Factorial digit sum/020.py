def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n/10)

print "Answer:", sum_digits(fact(100))
